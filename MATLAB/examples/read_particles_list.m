% read_particles_list.m: Template for reading Particles List

%% Load object from pradformat file
h5filename = fullfile('outs', 'myparticles.h5');
plist = prad_load(h5filename);

%% Examine your newly loaded object
disp(plist)

%% Utilize object's datasets and attributes in your own scripts
assert(isa(plist, 'ParticlesList'));

% plist.x; % required | x position of particle | meters
% plist.y; % required | y position of particle | meters
% plist.z; % required | z position of particle | meters
% plist.px; % required | momentum of particle, x-component | kg * m/s
% plist.py; % required | momentum of particle, y-component | kg * m/s
% plist.pz; % required | momentum of particle, z-component | kg * m/s
% plist.charge; % required | particle charge | Coulombs
% plist.mass; % required | particle mass | kg
% plist.energy; % optional | particle energy (can be derived from px,py,pz,mass) | eV
% plist.spec_name; % optional | particle species name (e.g. "p+")*
% plist.weight; % optional | for pseudoparticles, number of real particles represented | real particles / pseudoparticle
% plist.id; % optional | unique particle ID (e.g. 4073)
%
% plist.object_type; % required | Specification of the HDF5 object type | "particles" (always this value)
% plist.particles_type; % required | Specification of the particles sub-type | "list" (always this value)
% plist.pradformat_version; % required | HDF5 pradformat file format version followed | e.g. "0.1.0"
% plist.shuffled; % optional | Whether the order of particles in this list has been randomly shuffled. 0 for false, 1 for true.
% plist.label; % optional | Short, identifying label for this file (with no spaces or crazy characters). This can be stamped onto plots, etc.
% plist.description; % optional | Longer description of this file. This can be read by people trying to figure out where this file came from.
% plist.file_date; % automatically-set | Date the (future) file will be created, in the format "YYYY-MM-DD" | You don't need to set this, it will be set automatically
% plist.raw_data_filename; % optional | Filename of the raw data file (e.g. simulation output) from which this derivative file was created, if applicable.

% Dealing with required attributes/datasets
disp(plist.pradformat_version)
disp(mean(plist.px(:)))

% Dealing with optional attributes/datasets
if ~isempty(plist.label)
    disp(plist.label)
else
    disp("Well, I'd like to show you the label attribute, but I guess it wasn't set. Oh well.")
end

%%  Asterixed footnotes referenced above:
%
%  * For best compatibility, consider using the PlasmaPy particle symbol conventions. https://docs.plasmapy.org/en/stable/api/plasmapy.particles.particle_symbol.html
%     For example, protons can be specified as just "p+", and electrons by "e-". Any arbitrary isotope of Hydrogen can be specified "H-I q+"? where I is the mass number and q is the charge.
%