function obj = read_simple_fields(h5filename)
    % read_simple_fields Read simple fields data from HDF5 file
    obj = simple_fields;
    % TODO: Check that this matches the requirements
    % obj.object_type = h5readatt(h5fn, '/', 'object_type');
    % obj.fields_type = h5readatt(h5fn, '/', 'fields_type');
    obj.pradtools_version = h5readatt(h5filename, '/', 'pradtools_version');

    % Read fields HDF5 file into this object
    obj.X = h5read(h5filename, '/X');
    obj.Y = h5read(h5filename, '/Y');
    obj.Z = h5read(h5filename, '/Z');
    obj.Ex = h5read(h5filename, '/Ex');
    obj.Ey = h5read(h5filename, '/Ey');
    obj.Ez = h5read(h5filename, '/Ez');
    obj.Bx = h5read(h5filename, '/Bx');
    obj.By = h5read(h5filename, '/By');
    obj.Bz = h5read(h5filename, '/Bz');
    try obj.rho = h5read(h5filename, '/rho'); catch; end
    try obj.rho_description = h5readatt(h5filename, '/', 'rho_description'); catch; end
end