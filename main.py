"""
The nine discrete facies (classes of rocks) are:
1 = Nonmarine sandstone
2 = Nonmarine coarse siltstone
3 = Nonmarine fine siltstone
4 = Marine siltstone and shale
5 = Mudstone (limestone)
6 = Wackestone (limestone)
7 = Dolomite
8 = Packstone-grainstone (limestone)
9 = Phylloid-algal bafflestone (limestone)
"""

from os.path import join

from pandas import read_csv, options, set_option

from matplotlib.pyplot import close

from visualization import make_facies_log_plot

close('all')

set_option("display.max_rows", 10)
options.mode.chained_assignment = None

if __name__ == '__main__':
    file_path = join('data_input', 'facies_vectors.csv')

    well_data = read_csv(file_path)
    well_data.set_index('Well Name', inplace=True)

    well_names = well_data.index.unique()
    num_wells = len(well_names)

    print("There are 10 wells in *.csv file:")
    [print("  - %s" % well_name) for well_name in well_names]

    blind_well = well_data.loc['SHANKLE']
    training_data = well_data.drop('SHANKLE')
    training_wells = training_data.index.unique()

    training_data.loc[:,'FaciesLabels'] = training_data.apply(lambda row: FACIES_LABELS[(row['Facies'])], axis=1)
    training_data.describe()
    # # Plot all wells
    # for well in training_wells:
    #     make_facies_log_plot(training_data.loc[well], FACIES_COLORS)
