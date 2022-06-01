
# ##WB IMPORTS
import os
import numpy as np
import math as m
from scipy.signal import savgol_filter, find_peaks
from sklearn.linear_model import LinearRegression
from scipy.interpolate import interp1d
from B_SCR.plots import plot_sec_der_peaks

# Used to convert the LD Data to True Stress and Plastic Strain
def convert_stress_strain(path, gauge_length, diameter):

    data = np.genfromtxt(path, unpack=True, delimiter=',', skip_header=2)
    force = data[1, :]  # creates RF array from first column
    disp = data[0, :]  # Creates U array from second column

    # ##GET MAX DISPLACEMENT
    max_disp = disp[-1]

    uts_index = np.argmax(force)

    eng_stress = np.divide(force[:uts_index + 1], m.pi * (float(diameter) / 2) ** 2) * 1000
    eng_strain = np.divide(disp[:uts_index + 1], float(gauge_length) / 2)

    true_strain = np.log(1 + eng_strain)
    true_stress = eng_stress * (1 + eng_strain)

    return true_strain, true_stress, max_disp, force, disp


def aoc_calc_slope(true_strain, true_stress):
    """ function to calculate the slope of the extrapolated true stress-strain curve.
    function returns the minimum and maximum potential slopes based on five data points
    preceeding the UTS position. """
    # ##INTERESTED IN SLOPE BASED ON UTS AND PRECEEDING 5 POINTS
    # ##CAN'T EXTRAPOLATE BASED ON A SINGLE DATA POINT SO RANGE
    # ##MUST GOT FROM TWO TO SEVEN
    for i in range(2, 7, 1):
        stress = true_stress[-i:].reshape(-1, 1)
        strain = true_strain[-i:].reshape(-1, 1)
        model = LinearRegression().fit(strain, stress)
        c_slope = model.coef_[0][0]
        # ##FOR FIRST ITERATION SET BOTH MIN AND MAX VALUES TO CURRENT SLOPE
        if (i == 2):
            min_slope = c_slope
            max_slope = c_slope
        # ## FOR ALL OTHER ITERATIONS MODIFY THE MIN AND MAX
        elif (i > 2):
            if c_slope > max_slope:
                max_slope = c_slope
            elif c_slope < min_slope:
                min_slope = c_slope

    return min_slope, max_slope

def second_derivative_strain(true_strain, true_stress, **path_dic):

    # ##DATA ARE VERY SPARSE SO WE'RE GOING TO INTERPOLATE BETWEEN EACH POINT OF THE CURVE USING A SPLINE
    func = interp1d(true_strain, true_stress, kind='cubic')
    interp_strain = np.arange(true_strain[0], true_strain[-1], 1e-4)
    interp_stress = func(interp_strain)

    sder_strain = savgol_filter(interp_strain, window_length=41, polyorder=3, deriv=2)

    # FIND THE PEAK MAXIMA VALUES
    max_peaks, _ = find_peaks(sder_strain)
    # PLOT
    plot_sec_der_peaks(true_strain, true_stress, interp_strain, interp_stress, sder_strain, max_peaks[0], **path_dic)
    # ##GET YIELD STRESS ASSOCIATED WITH PEAK (FIRST ONE ONLY)
    yield_stress = interp_stress[max_peaks[0]]
    # ##CALCULATE MODULUS
    mod_strain = interp_strain[:max_peaks[0]].reshape(-1, 1)
    mod_stress = interp_stress[:max_peaks[0]].reshape(-1, 1)
    model = LinearRegression().fit(mod_strain, mod_stress)
    youngs_modulus = model.coef_[0][0]

    return round(yield_stress, 2), round(youngs_modulus, 2), interp_strain, interp_stress

def aoc_plastic_prop(strain, stress, yield_stress, modulus):
    '''CALCULATE Y-INTERCEPT FROM STRESS,
        PLASTIC STRAIN AND SLOPE'''
    stress = stress.tolist()
    strain = strain.tolist()

    # ##FIND YIELD POINT AND IGNORE ALL VALUES PREVIOUS TO THAT POINT
    ind = (abs(stress-yield_stress)).argmin()
    stress = stress[ind:]
    strain = strain[ind:]

    # ##CALCULATE PLASTIC STRAIN FROM TRUE STRAIN
    plastic_strain = strain - (stress / modulus)
    # ##FIRST PLASTIC STRAIN VALUE IN ABAQUS MUST BE ZERO SO WE NEED TO ZERO THE ARRAY
    plastic_strain = plastic_strain - plastic_strain[0]
    # ##ONLY POSITIVE STRAINS ALLOWED - INDEX NEGATIVE VALUES AND REMOVE FROM BOTH STRESS AND STRAIN ARRAYS
    pos_vals = [(round(stress[i], 3), plastic_strain[i]) for i, val in enumerate(plastic_strain) if val >= 0]
    uts_point = pos_vals[-1]

    return pos_vals, uts_point

def slope_range_calc(min_m, max_m, num_inc):
    inc_val = (max_m - min_m) / num_inc
    return np.arange(min_m, (max_m + inc_val), inc_val).tolist()