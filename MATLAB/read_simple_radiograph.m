function obj = read_simple_radiograph(h5filename)
    % read_simple_radiograph Read simple radiograph data from HDF5 file
    obj = simple_radiograph;

    % Check that the filetype matches and that we're using an up-to-date
    % pradformat reader toolbox (or move on if version comparison fails).
    object_type = h5readatt(h5filename, '/', 'object_type');
    assert(strcmp(object_type, obj.object_type));
    radiograph_type = h5readatt(h5filename, '/', 'radiograph_type');
    assert(strcmp(radiograph_type, obj.radiograph_type));

    pradformat_version = h5readatt(h5filename, '/', 'pradformat_version');
    try
        ver_file = strsplit(pradformat_version, '.');
        ver_tbox = strsplit(obj.pradformat_version, '.');
        if ver_tbox{0}
        if verLessThan('pradformat', pradformat_version)
            warning('Your MATLAB pradformat toolbox is out of date. This file was generated with a more recent version. Please download the latest pradformat toolbox by visiting "https://github.com/phyzicist/pradformat".')
        end
    catch
        warning("Failed to identify whether your pradformat toolbox version is up-to-date with the file format version you're reading. Proceed with caution!")
    end

    % Read in required datasets
    for i=1:length(obj.req_ds)
        ds = obj.req_ds(i);
        try
            data = h5read(h5filename, ['/' char(ds)]);
            set(obj, ds, data);
        catch
            warning(['Failed to read in expected dataset "' char(ds) '". Could it be missing from this file?'])
        end
    end

    % Read in optional datasets
    for i=1:length(obj.opt_ds)
        ds = obj.opt_ds(i);
        try
            data = h5read(h5filename, ['/' char(ds)]);
            set(obj, ds, data);
        catch
        end
    end

    % Read in required attributes
    for i=1:length(obj.req_atts)
        att = obj.req_atts(i);
        if ~any(strcmp(att, ["object_type", "radiograph_type"])) % These are fixed, set by the class definition; don't try to set these.
            try
                data = h5readatt(h5filename, '/', att);
                set(obj, att, data);
            catch
                warning(['Failed to read in expected attribute "' char(att) '". Could it be missing from this file?'])
            end
        end
    end

    % Read in optional attributes
    for i=1:length(obj.opt_atts)
        att = obj.opt_atts(i);
        try
            data = h5readatt(h5filename, '/', att);
            set(obj, att, data);
        catch
        end
    end
end