% example4_advanced_radiograph.py: Read and write the simple radiograph format for HDF5 pradtools

% Example RCF layer radiograph for 25 MeV protons (but with some sensitivity to higher energy protons)

% Construct object
rad = AdvancedRadiograph;
rad.label = "MarchDISC_RCF_layer3";
rad.description = "Layer 3 of the RCF stack on shot number 2 at OMEGA 2021 DISC. This layer is primarily sensitive to 25 MeV protons";
rad.experiment_date = "2021-02-29";

nx = 100;
ny = 300;
rad.image = randi(5000, nx, ny); % Random radiograph image of this RCF layer
rad.pixel_width = 100.0e-6; % 100-micron bin size
rad.source_distance = 1.53; % Proton source was 1.53 meters from the RCF layer
rad.ROI_distance = 1.45; % Plasma of interest was 1.45 meters from the RCF layer

rad.sensitivities = {}; % Must always be a cell array, even if only one species is included

% Proton sensitivity
s = Sensitivity;
s.spec_name = "p+";
s.spec_mass = 1.673e-27; % proton mass in kg
s.spec_charge = 1.602e-19; % proton charge in Coulombs
s.energies = [20.0, 25.0, 30.0, 40.0]; % energies for which sensitivities are characterized for this species
s.scale_factors = [1.0e20, 1.0e18, 1.0e19, 1.5e19]; % incident particles/pixel-count for these energies (factoring in the layers in front of this RCF layer)
rad.sensitivities{end + 1} = s; % append this sensitivity to the cell array

% Electron sensitivity
s = Sensitivity;
s.spec_name = "e-";
s.spec_mass = 9.109e-31;  % electron mass in kg
s.spec_charge = -1.602e-19; % electron charge in Coulombs (note negative sign)
s.energies = [20.0, 100.0, 200.0]; % energies for which sensitivities are characterized for this species
s.scale_factors = [1.0e21, 1.0e20, 1.0e19]; % incident particles/pixel-count for these energies (factoring in the layers in front of this RCF layer)
rad.sensitivities{end + 1} = s; % append this sensitivity to the cell array

% Save to file
[status, msg, msgID] = mkdir('outs');
h5filename = fullfile('outs', 'example4-o1.h5');
prad_save(rad, h5filename);

% Pretty print your radiograph object and its sensitivities
disp(rad)
for i=1:numel(rad.sensitivities)
    disp(rad.sensitivities{i})
end

% For demo purposes, read back in the file you just saved, then write it
% again
rad2 = prad_load(h5filename);
h5filename = fullfile('outs', 'example4-o2.h5');
prad_save(rad2, h5filename);