function obj = read_simple_radiograph(h5filename)
    % read_simple_radiograph Read a simple radiograph from HDF5 file
    obj = simple_radiograph;
    % TODO: Check that this matches the requirements
    % obj.object_type = h5readatt(h5fn, '/', 'object_type');
    % obj.radiograph_type = h5readatt(h5fn, '/', 'radiograph_type');
    obj.pradtools_version = h5readatt(h5filename, '/', 'pradtools_version');

    % Read monochromatic radiograph HDF5 file into this object
    obj.image = h5read(h5filename, '/image');
    try obj.X = h5read(h5filename,'/X'); catch ; end % TODO: Handle this better
    try obj.Y = h5read(h5filename,'/Y'); catch ; end
    try obj.Z = h5read(h5filename,'/Z'); catch ; end
    obj.pixel_width = h5readatt(h5filename, '/', 'pixel_width');
    obj.pradtools_version = h5readatt(h5filename, '/', 'pradtools_version');
    obj.scale_factor = h5readatt(h5filename, '/', 'scale_factor');
    try obj.source_distance = h5readatt(h5filename, '/', 'source_distance'); catch ; end
    try obj.ROI_distance = h5readatt(h5filename, '/', 'ROI_distance'); catch ; end
    try obj.spec_name = h5readatt(h5filename, '/', 'spec_name'); catch ; end
    try obj.spec_mass = h5readatt(h5filename, '/', 'spec_mass'); catch ; end
    try obj.spec_charge = h5readatt(h5filename, '/', 'spec_charge'); catch ; end
    try obj.spec_energy = h5readatt(h5filename, '/', 'spec_energy'); catch ; end
end