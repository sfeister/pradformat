function obj = prad_load(h5filename)
    % prad_load Read in any supported pradformat HDF5 file format
    % TODO: Check that this matches the requirements
    assert(isfile(h5filename))
    
    try
        info = h5info(h5filename);
    catch
        error("Error. \nCould not read basic HDF5 file info. Are you sure this is an HDF5 file?")
    end
    
    try
        object_type = h5readatt(h5filename, '/', 'object_type');
    catch
        error("Error. \nFailure to read the required 'object_type' attribute. See pradformat format specifications for details.")
    end
    
    switch char(object_type)
        case 'radiograph'
            try
                radiograph_type = h5readatt(h5filename, '/', 'radiograph_type');
            catch
                error("Error. \nFailure to read the required 'radiograph_type' attribute. See pradformat format specifications for details.")
            end
            switch char(radiograph_type)
                case 'simple'
                    obj = read_simple_radiograph(h5filename);
                case 'advanced'
                    obj = read_advanced_radiograph(h5filename);
                otherwise
                    error("Error. \n'%s' is not a recognized 'radiograph_type'. See pradformat format specifications for details.", radiograph_type);
            end
        case 'fields'
            try
                fields_type = h5readatt(h5filename, '/', 'fields_type');
            catch
                error("Error. \nFailure to read the required 'fields_type' attribute. See pradformat format specifications for details.")
            end
            switch char(fields_type)
                case 'simple'
                    obj = read_simple_fields(h5filename);
                otherwise
                    error("Error. \n'%s' is not a recognized 'fields_type'. See pradformat format specifications for details.", fields_type);
            end
        case 'particles'
            try
                particles_type = h5readatt(h5filename, '/', 'particles_type');
            catch
                error("Error. \nFailure to read the required 'particles_type' attribute. See pradformat format specifications for details.")
            end
            switch char(particles_type)
                case 'list'
                    obj = read_particles_list(h5filename);
                otherwise
                    error("Error. \n'%s' is not a recognized 'particles_type'. See pradformat format specifications for details.", particles_type);
            end
        otherwise
            error("Error. \n'%s' is not a recognized 'object_type'. See pradformat format specifications for details.", object_type);
    end
end