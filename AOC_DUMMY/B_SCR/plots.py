import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams["figure.figsize"] = (6, 6)
##set font size
font={'family': 'sans-serif',
      'weight': 'normal',
      'size':14}
plt.rc('font', **font)
import pandas as pd

def plot_sec_der_peaks(true_strain, true_stress, interp_strain, interp_stress, sder_strain, max_peaks, **path_dic):
    # PLOT TO SHOW THE CURVE AND SECOND DERIV
    fig, ax2d = plt.subplots()
    ax = np.ravel(ax2d)
    ax2 = ax[0].twinx()
    # PLOT DATA
    p1 = ax[0].plot(true_strain, true_stress, marker='o', color='k', linestyle=None, label='experimental data')
    p2 = ax[0].plot(interp_strain, interp_stress, color='k', linestyle='--', label='interpolated data')
    p3 = ax2.plot(interp_strain, sder_strain, color='r', label='second derivative of strain')
    # PLOT PEAKS
    p4 = ax2.plot(interp_strain[max_peaks], sder_strain[max_peaks],
                  'gx', label='end of linear region')
    p5 = ax[0].plot(interp_strain[max_peaks], interp_stress[max_peaks], 'gx', label='identified yield strength')

    # AXES LIMITS
    ax[0].set_xlim([0, max(true_strain) + (max(true_strain) * 0.1)])
    ax[0].set_ylim([0, max(interp_stress) + (max(interp_stress) * (0.1))])

    # AT LEAST FIVE TICK MARKS ON X AND Y AXES
    ax[0].xaxis.set_major_locator(plt.MaxNLocator(6))
    ax[0].yaxis.set_major_locator(plt.MaxNLocator(6))
    ax2.yaxis.set_major_locator(plt.MaxNLocator(6))

    # FORMAT XLABELS TO BE % RATHER THAN mm/mm
    locs, labels = plt.xticks()
    labels = [round(float(item) * 100, 2) for item in locs]
    plt.xticks(locs, labels)

    # AXES LABELS
    ax[0].set_xlabel('True strain, %')
    ax[0].set_ylabel('True stress, MPa')
    ax2.set_ylabel('Second order derivative')

    mylines = p1 + p2 + p3 + p4 + p5
    labs=[l.get_label() for l in mylines]
    ax[0].legend(mylines, labs, bbox_to_anchor=(1.1, 1), loc='upper left', borderaxespad=0)
    # ##save figure
    plt.savefig(os.path.join(path_dic['curr_results'], 'SECOND_ORDER.png'), dpi=300,
                bbox_inches='tight')

def force_disp(**path_dic):
    """ PLOT THE FORCE VERSUS DISPLACEMENT
    COMPARE EXPERIMENTAL DATA TO SIMULATED DATA.
    WE NEED TO SHOW PERFECT MATCH UP TO UTS"""
    fig, ax2d = plt.subplots()
    ax = np.ravel(ax2d)
    # ##IDENTIFY FORCE VERSUS DISPLACEMENT DATA
    data_list = [k for k in path_dic.keys() if '_fvd' in k]
    for i, data in enumerate(data_list):
        if 'exp' in data:
            df = pd.read_csv(path_dic[data], header=[0, 1]).droplevel(1, axis=1)
            ax[0].plot(df.iloc[:, 0], df.iloc[:, 1], color='k', label='experimental')
            cmf = max(df.iloc[:, 1])
            cmd = max(df.iloc[:, 0])
        else:
            df = pd.read_csv(path_dic[data], header=[0])
            ax[0].plot(df.iloc[:, 1], df.iloc[:, 0]/1000, linestyle='--', label=data[:data.rfind('_')])
            cmf = max(df.iloc[:, 0]/1000)
            cmd = max(df.iloc[:, 1])
        if i == 0:
            max_force = cmf
            max_disp = cmd
        elif i > 0:
            if cmf >= max_force:
                max_force == cmf
            if cmd >= max_disp:
                max_disp == cmd

    # AXES LIMITS
    ax[0].set_xlim([0, (1.1 * max_disp)])
    ax[0].set_ylim([0, (1.1 * max_force)])

    # AT LEAST FIVE TICK MARKS ON X AND Y AXES
    ax[0].xaxis.set_major_locator(plt.MaxNLocator(6))
    ax[0].yaxis.set_major_locator(plt.MaxNLocator(6))
    # AXES LABELS
    ax[0].set_xlabel('Force, kN')
    ax[0].set_ylabel('Displacement, mm')

    ax[0].legend(bbox_to_anchor=(1.1, 1),
                 loc='upper left',
                 borderaxespad=0)
    # save figure
    plt.savefig(os.path.join(path_dic['curr_results'], 'COMPARE_FVD.png'),
                dpi=300,
                bbox_inches='tight')
    # plt.show()

def mape_num_elem(**path_dic):
    # PLOT TO SHOW THE CURVE AND SECOND DERIV
    fig, ax2d = plt.subplots()
    ax = np.ravel(ax2d)

    df = pd.read_csv(path_dic['output_results'])

    for i, rw in df.iterrows():
        ax[0].scatter(rw['TIME'], rw['MAPE'], label='JOB' + str(i) + ' ELEMENTS: ' + str(int(rw['TOTAL_NUM_ELEM'])))

    # AT LEAST FIVE TICK MARKS ON X AND Y AXES
    ax[0].xaxis.set_major_locator(plt.MaxNLocator(6))
    ax[0].yaxis.set_major_locator(plt.MaxNLocator(6))
    # AXES LABELS
    ax[0].set_xlabel('Time, seconds')
    ax[0].set_ylabel('Mean absolute percentage error (MAPE), %')

    ax[0].legend(bbox_to_anchor=(1.1, 1),
                 loc='upper left',
                 borderaxespad=0)
    # save figure
    plt.savefig(os.path.join(path_dic['curr_results'], 'MAPE.png'),
                dpi=300,
                bbox_inches='tight')
    # plt.show()


def boxplot(x_var, y_var, df, savepath=os.getcwd(), savename='PLOT', ylabel='Value'):
    fig, ax = plt.subplots()
    ax = sns.boxplot(x=x_var,
                     y=y_var,
                     data=df,
                     showmeans=True,
                     palette='Set2')
    ax = sns.swarmplot(x=x_var,
                       y=y_var,
                       data=df,
                       color=".25")

    # AXES LABELS
    ax.set_xlabel('Parameter')
    ax.set_ylabel(ylabel)
    # ##save figure
    plt.savefig(os.path.join(savepath, savename + '_BPLT.png'), dpi=300,
                bbox_inches='tight')
    plt.show()

def heatmap(df, savepath=os.getcwd(), savename='PLOT', ylabel='Value'):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(abs(df.corr(method='pearson')),
                vmin=0,
                vmax=1,
                ax=ax,
                annot=True, fmt='.2f')
    plt.savefig(os.path.join(savepath, savename + '_HMAP.png'), dpi=300,
                bbox_inches='tight')
    plt.show()

def plot_decision_regions(X=None,
                          y=None,
                          classifer=None,
                          test_idx=None,
                          resolution=0.02,
                          root=None,
                          filename=None):
    markers = ('o', 's', '^', 'v', '<')
    colors=('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    fig, ax = plt.subplots()
    x1min, x1max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2min, x2max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1min, x1max, resolution),
                           np.arange(x2min, x2max, resolution))
    lab=classifer.predict(np.array([xx1.ravel(),
                                    xx2.ravel()]).transpose())
    lab = lab.reshape(xx1.shape)
    plt.contourf(xx1,
                 xx2,
                 lab,
                 alpha=0.3,
                 cmap=cmap)
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y==cl, 0],
                    y=X[y==cl, 1],
                    alpha=0.8,
                    c=colors[idx],
                    marker=markers[idx],
                    label='Class %s'%(cl))

def scree_plot(principal_components=None, yheight=None, tick_lab=None, savepath=None,
               savename=None, title=None):
    fig, ax = plt.subplots()
    ax.bar(x=principal_components,
            height=yheight,
            tick_label=tick_lab)
    plt.title(title)
    plt.ylabel('Percentage of Explained Variance, %')
    plt.xlabel('Principal Component')
    plt.savefig(os.path.join(savepath, savename + '.png'),
                dpi=300,
                bbox_inches='tight')
    plt.show()

def pca_2d(dataframe=None, variation_data=None, title=None,
           savepath=None, savename=None):
    fig, ax = plt.subplots()
    ax.scatter(x=dataframe.iloc[:, 0], y=dataframe.iloc[:, 1])
    plt.xlabel('PC1, {0}%'.format(variation_data[0]))
    plt.ylabel('PC2, {0}%'.format(variation_data[1]))
    plt.title(title)
    for sample in dataframe.index:
        ax.annotate(sample,
                     (dataframe.loc[sample].iloc[0], dataframe.loc[sample].iloc[1]))
    plt.savefig(os.path.join(savepath, savename + '.png'),
                dpi=300,
                bbox_inches='tight')
    plt.show()

def pca_3d(dataframe=None, variation_data=None, title=None,
           savepath=None, savename=None):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(xs=dataframe.iloc[:, 0],
               ys=dataframe.iloc[:, 1],
               zs=dataframe.iloc[:, 2])
    ax.set_xlabel('PC1, {0}%'.format(variation_data[0]))
    ax.set_ylabel('PC2, {0}%'.format(variation_data[1]))
    ax.set_zlabel('PC3, {0}%'.format(variation_data[2]))
    plt.title(title)
    # for sample in dataframe.index:
    #     plt.annotate(sample,
    #                  (dataframe.iloc[sample, 0],
    #                   dataframe.iloc[sample, 1],
    #                   dataframe.iloc[sample, 2]))
    plt.savefig(os.path.join(savepath, savename + '.png'),
                dpi=300,
                bbox_inches='tight')
    plt.show()