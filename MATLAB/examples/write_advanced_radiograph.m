% write_advanced_radiograph.m: A template for writing your own Advanced Radiograph

%% Construct Advanced Radiograph object
rad = AdvancedRadiograph;

%% Set datasets and attributes (except sensitivities)
M = 900; % image first dimension
N = 700; % image second dimension

rad.image = zeros(M, N); % required | Radiograph image (cropped and rotated, if desired) | pixel count
% rad.X = zeros(M, N); % optional | X position of pixel centers (radiograph coordinate system*) | meters
% rad.Y = zeros(M, N); % optional | Y position of pixel centers (radiograph coordinate system*) | meters
% rad.T = zeros(3,3); % optional | Change-of-basis matrix (a.k.a. transition matrix) to move from x, y, z radiograph coordinate system* to x', y', z' global coordinate system of the target chamber. [x' y' z'] = T [x y z].

% disp(rad.object_type) % already-set | Specification of the HDF5 object type | "radiograph" (always this value)
% disp(rad.radiograph_type) % already-set | Specification of the radiograph sub-type | "advanced" (always this value)
% disp(rad.pradformat_version) % already-set | HDF5 pradformat file format version followed | e.g. "0.1.0"

rad.pixel_width = 100.0e-6; % required | Physical pixel width / bin width, for the first image axis | meters
% rad.pixel_width_ax2 = 25.0e-6; % optional | Physical pixel width / bin width, for the second image axis (not needed if using square pixels) | meters
rad.source_distance = 1.53; % optional | Approximate distance from the particle source to the plane of the radiograph | meters
rad.ROI_distance = 1.45; % optional | Approximate distance from the center of the imaged region of interest to the plane of the radiograph | meters

rad.label = "MarchDISC_RCF_layer3"; % optional | Short, identifying label for this file (with no spaces or crazy characters). This can be stamped onto plots, etc.
rad.description = "Layer 3 of the RCF stack on shot number 2 at OMEGA 2021 DISC. This layer is primarily sensitive to 25 MeV protons"; % optional | Longer description of this file. This can be read by people trying to figure out where this file came from.
rad.experiment_date = "2021-02-29"; % optional | Date of the experiment (or synthetic particle tracing), in the format "YYYY-MM-DD".
% disp(rad.file_date); % automatically-set | Date the (future) file will be created, in the format "YYYY-MM-DD" | You don't need to set this, it will be set automatically
rad.raw_data_filename = "20210231_color_scan.csv"; % optional | Filename of the raw data file (e.g. CSV from MIT, Tiff from scanner, etc) from which this derivative file was created, if applicable.

%% For each contributing species, set sensitivity datasets and attributes
rad.sensitivities = {}; % optional | a cell array filled with Sensitivity objects (one for each species) | must always be a cell array, even if only one species is included

% Electron sensitivity
s = Sensitivity;
s.spec_name = "e-"; % required | Shortname for the particle species (for this group)**
s.spec_mass = 9.109e-31;  % required | Particle mass (for this group) | kg
s.spec_charge = -1.602e-19; % (note negative sign) % required | Particle charge (for this group) | Coulombs
s.energies = [20.0, 100.0, 200.0]; % required | Particle energy represented by each element of the scale_factors array
s.scale_factors = [1.0e21, 1.0e20, 1.0e19]; % required | Multipliers to convert pixel counts into particle counts (wrapping in the effects of all prior layers in the detector stack)
s.prescale_factors = [1.0, 0.9, 1.1]; % optional | Pre-multipliers by which to adjust the scale factors (e.g. a fudge factor to adjust for RCF batch-to-batch sensitivity differences unrelated to stopping distance)

rad.sensitivities{end + 1} = s; % append this sensitivity to the cell array

% Proton sensitivity
s = Sensitivity;
s.spec_name = "p+";
s.spec_mass = 1.673e-27; % proton mass in kg
s.spec_charge = 1.602e-19; % proton charge in Coulombs
s.energies = [20.0, 25.0, 30.0, 40.0]; % energies for which sensitivities are characterized for this species
s.scale_factors = [1.0e20, 1.0e18, 1.0e19, 1.5e19]; %  Multipliers to convert pixel counts into particle counts (wrapping in the effects of all prior layers in the detector stack)

rad.sensitivities{end + 1} = s; % append this sensitivity to the cell array

%% Pretty print your newly-minted radiograph object and its sensitivities
disp(rad)
for i=1:numel(rad.sensitivities)
    disp(rad.sensitivities{i})
end

%% Save to file
[status, msg, msgID] = mkdir('outs');
h5filename = fullfile('outs', 'myradiograph2.h5');
prad_save(rad, h5filename);

%%  Asterixed footnotes referenced above:
%
%  * The convention of this format is that the image lies in the z=0 plane of the radiograph coordinate system, and that the z-axis will point towards the particle source. The image may be stored already cropped and rotated by any angle within the x-y radiograph coordinate system, which is why X and Y are specified as arrays rather than vectors.
%
%  ** For best compatibility, consider using the PlasmaPy particle symbol conventions. https://docs.plasmapy.org/en/stable/api/plasmapy.particles.particle_symbol.html
%     For example, protons can be specified as just "p+", and electrons by "e-". Any arbitrary isotope of Hydrogen can be specified "H-I q+"? where I is the mass number and q is the charge.
%