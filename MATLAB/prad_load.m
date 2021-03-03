function obj = prad_load(h5filename)
    % prad_load Read any HDF5 file of a supported pradformat (e.g.
    % SimpleRadiograph, SimpleFields, etc.) into a MATLAB object

    if ~(exist(h5filename, 'file') == 2)
        error(['Error.' newline 'File does not exist: ' char(h5filename)]);
    end
    
    try
        h5info(h5filename);
    catch
        error(['Error.' newline 'Could not read basic HDF5 file info. Are you sure this is an HDF5 file?']);
    end
    
    try
        file_pradformat_version = h5readatt(h5filename, '/', 'pradformat_version');
    catch
        error(['Error.' newline 'Failure to read the required "pradformat_version" attribute from within this HDF5 file. See pradformat format specifications for details.']);
    end
    
    try
        if verparse(file_pradformat_version) > verparse(pradformat_version())
            warning(['Your MATLAB pradformat toolbox is out of date. The file you are about to load was generated with version ' char(file_pradformat_version) ', but your toolbox version is only ' char(pradformat_version()) '. For best compatibility, download the latest pradformat toolbox by visiting "https://github.com/phyzicist/pradformat".']);
        end
    catch
        warning('Failed to identify whether your pradformat toolbox version is up-to-date with the file format version you''re reading. Proceed with caution!');
    end

    try
        object_type = h5readatt(h5filename, '/', 'object_type');
    catch
        error(['Error.' newline 'Failure to read the required "object_type" attribute from within this HDF5 file. See pradformat format specifications for details.']);
    end
    
    switch char(object_type)
        case 'radiograph'
            try
                radiograph_type = h5readatt(h5filename, '/', 'radiograph_type');
            catch
                error(['Error.' newline 'Failure to read the required "radiograph_type" attribute from within this HDF5 file. See pradformat format specifications for details.']);
            end
            switch char(radiograph_type)
                case 'simple'
                    obj = SimpleRadiograph(h5filename);
                case 'advanced'
                    obj = AdvancedRadiograph(h5filename);
                otherwise
                    error(['Error.' newline '"' char(radiograph_type) 'is not a recognized "radiograph_type" from within this HDF5 file. See pradformat format specifications for details.']);
            end
        case 'fields'
            try
                fields_type = h5readatt(h5filename, '/', 'fields_type');
            catch
                error(['Error.' newline 'Failure to read the required "fields_type" attribute from within this HDF5 file. See pradformat format specifications for details.']);
            end
            switch char(fields_type)
                case 'simple'
                    obj = SimpleFields(h5filename);
                otherwise
                    error(['Error.' newline '"' char(fields_type) '" is not a recognized "fields_type" from within this HDF5 file. See pradformat format specifications for details.']);
            end
        case 'particles'
            try
                particles_type = h5readatt(h5filename, '/', 'particles_type');
            catch
                error(['Error.' newline 'Failure to read the required "particles_type" attribute from within this HDF5 file. See pradformat format specifications for details.'])
            end
            switch char(particles_type)
                case 'list'
                    obj = ParticlesList(h5filename);
                otherwise
                    error(['Error.' newline '"' char(particles_type) '" is not a recognized "particles_type" from within this HDF5 file. See pradformat format specifications for details.']);
            end
        case 'inversion'
            try
                fields_type = h5readatt(h5filename, '/', 'inversion_type');
            catch
                error(['Error.' newline 'Failure to read the required "inversion_type" attribute from within this HDF5 file. See pradformat format specifications for details.']);
            end
            switch char(fields_type)
                case 'simple'
                    obj = SimpleInversion(h5filename);
                otherwise
                    error(['Error.' newline '"' char(fields_type) '" is not a recognized "inversion_type" from within this HDF5 file. See pradformat format specifications for details.']);
            end
        otherwise
            error(['Error.' newline '"' char(object_type) ' is the "object_type" read from within this HDF5 file, but that is not a supported "object_type". See pradformat format specifications for details.']);
    end
end