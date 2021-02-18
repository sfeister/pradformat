% example3_particles_list.m Read and write the Particles List format for
% HDF5 pradformat

% Example 100x300 CR39 radiograph for 14.7 MeV protons

% Construct object
plist = ParticlesList;

% Define some general attributes
plist.label = "ebeam_100MeV";
plist.description = "100 MeV electrons emitted uniformly into a 3-degree half-cone angle. Source size is 2 microns standard deviation, centered on (0,0,0).";

N = 1000; % Number of particles to generate

% Define particle positions
source_radius = 2.0e-6; % 2 micron for source radius (normal distribution standard deviation length)
R = normrnd(0, source_radius, N); % Radius is in a normal distribution of standard deviation source_radius
theta = unifrnd(0, pi, N); % theta is uniform from 0 to pi
phi = unifrnd(-pi, pi, N); % phi is uniform from -pi to pi

plist.x = R * sin(theta) * cos(phi);
plist.y = R * sin(theta) * sin(phi);
plist.z = R * cos(theta);


% Define particle momenta
pmag = 5.403e-21; % Magnitude of momentum for 100 MeV electron, in kg * m/s (I used Wolfram Alpha: https://www.wolframalpha.com/input/?i=100+MeV+electron+to+momentum)
half_angle = deg2rad(3.0); % Allow for a 3-degree half-angle conical divergence of particle emission
ptheta = unifrnd(0, half_angle, N);
pphi = unifrnd(-half_angle, half_angle, N);

plist.px = pmag * sin(ptheta) * cos(pphi);
plist.py = pmag * sin(ptheta) * sin(pphi);
plist.pz = pmag * cos(ptheta);

% Define additional particle attributes
plist.charge = -1.602e-19;
plist.mass = 9.109e-31;
plist.spec_name = "e-";
plist.id = 1:N;

% Save to file
[status, msg, msgID] = mkdir('outs');
h5filename = fullfile('outs', 'example3-o1.h5');
prad_save(plist, h5filename);

% For demo purposes, read back in the file you just saved, then write it
% again
plist2 = prad_load(h5filename);
h5filename = fullfile('outs', 'example3-o2.h5');
prad_save(plist2, h5filename);