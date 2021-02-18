% example1_simple_radiograph.m Read and write the simple radiograph format for
% HDF5 pradformat

% Example 100x300 CR39 radiograph for 14.7 MeV protons

% Construct object
rad = simple_radiograph; % Initialize "rad" as an object of class "simple_radiograph"

nx = 100;
ny = 300;
rad.image = randi(5000, nx, ny); % Random radiograph image
rad.pixel_width = 100.0e-6; % 100-micron bin size
rad.scale_factor = 1; % one pixel count represents one particle count
rad.source_distance = 1.53; % Proton source was 1.53 meters from the CR39
rad.ROI_distance = 1.45; % Plasma of interest was 1.45 meters from the CR39
rad.spec_name = "p+";
rad.spec_mass = 1.67262e-27; % proton mass in kg
rad.spec_charge = 1.6021766208e-19; % proton charge in Coulombs
rad.spec_energy = 14.7e6; % 14.7 MeV protons

% Save to file
[status, msg, msgID] = mkdir('outs');
h5filename = fullfile('outs', 'example1-o1.h5');
prad_save(rad, h5filename);

% For demo purposes, read back in the file you just saved, then write it
% again
rad2 = prad_load(h5filename);
h5filename = fullfile('outs', 'example1-o2.h5');
prad_save(rad2, h5filename);