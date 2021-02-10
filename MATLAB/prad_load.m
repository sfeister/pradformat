function obj = prad_load(h5filename)
    % prad_load Read in any supported pradtools HDF5 file format
    % TODO: Check that this matches the requirements
    info = h5info(h5filename);

    try
        object_type = h5readatt(h5filename, '/', 'object_type');
    catch
        error("Error. \nFailure to read the required 'object_type' attribute. See pradtools format specifications for details.")
    end
    
    switch object_type
        case 'radiograph'
            try
                radiograph_type = h5readatt(h5filename, '/', 'radiograph_type');
            catch
                error("Error. \nFailure to read the required 'radiograph_type' attribute. See pradtools format specifications for details.")
            end
            switch radiograph_type
                case "simple"
                    obj = read_simple_radiograph(h5filename);
                otherwise
                    error("Error. \n'%s' is not a recognized 'radiograph_type'. See pradtools format specifications for details.", radiograph_type);
            end
        case 'fields'
            try
                fields_type = h5readatt(h5filename, '/', 'fields_type');
            catch
                error("Error. \nFailure to read the required 'fields_type' attribute. See pradtools format specifications for details.")
            end
            switch fields_type
                case "simple"
                    obj = read_simple_fields(h5filename);
                otherwise
                    error("Error. \n'%s' is not a recognized 'fields_type'. See pradtools format specifications for details.", fields_type);
            end
        otherwise
            error("Error. \n'%s' is not a recognized 'object_type'. See pradtools format specifications for details.", object_type);
    end
end