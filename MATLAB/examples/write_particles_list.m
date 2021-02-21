% write_particles_list.m: A template for writing your own Particles List

%% Construct Particles List object
plist = ParticlesList;

%% Create some test 1D arrays (R, theta, and phi in position and momentum space)
N = 1000; % Number of particles to generate
source_radius = 2.0e-6; % 2 micron for source radius (normal distribution standard deviation length)
R = normrnd(0, source_radius, [1,N]); % Radius is in a normal distribution of standard deviation source_radius
theta = unifrnd(0, pi, [1,N]); % theta is uniform from 0 to pi
phi = unifrnd(-pi, pi, [1,N]); % phi is uniform from -pi to pi

% Define particle momenta
pmag = 5.403e-21; % Magnitude of momentum for 100 MeV electron, in kg * m/s (I used Wolfram Alpha: https://www.wolframalpha.com/input/?i=100+MeV+electron+to+momentum)
half_angle = deg2rad(3.0); % Allow for a 3-degree half-angle conical divergence of particle emission
ptheta = unifrnd(0, half_angle, [1,N]);
pphi = unifrnd(-half_angle, half_angle, [1,N]);

%% Set datasets and attributes of the Particles List object
plist.x = R .* sin(theta) .* cos(phi); % required | x position of particle | meters
plist.y = R .* sin(theta) .* sin(phi); % required | y position of particle | meters
plist.z = R .* cos(theta); % required | z position of particle | meters

plist.px = pmag .* sin(ptheta) .* cos(pphi); % required | momentum of particle, x-component | kg * m/s
plist.py = pmag .* sin(ptheta) .* sin(pphi); % required | momentum of particle, y-component | kg * m/s
plist.pz = pmag .* cos(ptheta); % required | momentum of particle, z-component | kg * m/s

plist.charge = -1.602e-19 * ones([1,N]); % required | particle charge | Coulombs
plist.mass = 9.109e-31 * ones([1,N]); % required | particle mass | kg
plist.energy = 100.0e6 * ones([1,N]); % optional | particle energy (can be derived from px,py,pz,mass) | eV
plist.spec_name = repelem("e-", N); % optional | particle species name (e.g. "p+")*
plist.weight = 100 * ones([1,N]); % optional | for pseudoparticles, number of real particles represented | real particles / pseudoparticle
plist.id = 1:N; % optional | unique particle ID (e.g. 4073)

% disp(plist.object_type) % already-set | Specification of the HDF5 object type | "particles" (always this value)
% disp(plist.particles_type) % already-set | Specification of the particles sub-type | "list" (always this value)
% disp(plist.pradformat_version) % already-set | HDF5 pradformat file format version followed | e.g. "0.1.0"

plist.shuffled = 0; % optional | Whether the order of particles in this list has been randomly shuffled. 0 for false, 1 for true.
plist.label = "Ebeam_100MeV"; % optional | Short, identifying label for this file (with no spaces or crazy characters). This can be stamped onto plots, etc.
plist.description = "100 MeV electron beam into a 3-degree half-angle cone, from a source with 2-micron standard-deviation length scale."; % optional | Longer description of this file. This can be read by people trying to figure out where this file came from.
% disp(plist.file_date); % automatically-set | Date the (future) file will be created, in the format "YYYY-MM-DD" | You don't need to set this, it will be set automatically
% plist.raw_data_filename = "/fs/EPOCH/mysim/sdf0013"; % optional | Filename of the raw data file (e.g. simulation output) from which this derivative file was created, if applicable.

%% Pretty print your newly-minted Particles List object
disp(plist)

%% Save to file
[status, msg, msgID] = mkdir('outs');
h5filename = fullfile('outs', 'myparticles.h5');
prad_save(plist, h5filename);

%%  Asterixed footnotes referenced above:
%
%  * For best compatibility, consider using the PlasmaPy particle symbol conventions. https://docs.plasmapy.org/en/stable/api/plasmapy.particles.particle_symbol.html
%     For example, protons can be specified as just "p+", and electrons by "e-". Any arbitrary isotope of Hydrogen can be specified "H-I q+"? where I is the mass number and q is the charge.
%