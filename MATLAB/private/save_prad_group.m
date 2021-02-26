function [] = save_prad_group(obj, h5filename, h5root)
%SAVE_PRAD_GROUP Save all optional/required group-level datasets/attributes of a prad object into an
%already-created group in an existing HDF5 file; h5grp should 
%   h5root should be something like "/" or "/mygrp/", and must end with a
%   forwardslash
    
    % Enforce h5root as char array and last character of h5root being a forward-slash
    h5root = char(h5root);
    if ~strcmp(h5root(end),  '/')
        h5root = strcat(h5root, '/');
    end

    % Write required datasets to file % TODO: Force a certain array
    % size
    for i=1:length(obj.req_ds)
        ds = char(obj.req_ds(i));
        data = get(obj, ds);
        if isempty(data)
            delete(h5filename); % delete this incomplete file
            error(['Required dataset is empty! This file will not meet pradformat specs. Empty dataset: ' char(ds) '. Please set a value and retry saving this file.'])
        elseif isstring(data) && verLessThan('matlab', '9.8')
            % skip dataset due to incompatibility
            warning(['Skipping writing required dataset "' char(ds) '" because writing string arrays to HDF5 is unsupported prior to MATLAB R2020a. Upgrade MATLAB to R2020a+ to avoid skipping over this dataset.'])
        elseif ~isscalar(data)
            % write compressed dataset
            h5create(h5filename, [h5root char(ds)], size(data),...
                'DataType', class(data), ...
                'ChunkSize', autochunksize(data), 'Deflate', 4);
            h5write(h5filename, [h5root char(ds)], data);
        else
            % write uncompressed dataset
            h5create(h5filename, [h5root char(ds)], size(data),...
                'DataType', class(data));
            h5write(h5filename, [h5root char(ds)], data);
        end
    end

    % Write optional datasets to file
    for i=1:length(obj.opt_ds)
        ds = char(obj.opt_ds(i));
        data = get(obj, ds);
        if isempty(data)
            % do nothing
        elseif isstring(data) && verLessThan('matlab', '9.8')
            % skip dataset due to incompatibility
            warning(['Skipping writing optional dataset "' char(ds) '" because writing string arrays to HDF5 is unsupported prior to MATLAB R2020a. Upgrade MATLAB to R2020a+ to avoid skipping over this dataset.'])
        elseif ~isscalar(data)
            % write compressed dataset
            h5create(h5filename, [h5root char(ds)], size(data),...
                'DataType', class(data), ...
                'ChunkSize', autochunksize(data), 'Deflate', 4);
            h5write(h5filename, [h5root char(ds)], data);
        else
            % write uncompressed dataset
            h5create(h5filename, [h5root char(ds)], size(data),...
                'DataType', class(data));
            h5write(h5filename, [h5root char(ds)], data);
        end
    end

    % Write required attributes to file
    for i=1:length(obj.req_atts)
        att = char(obj.req_atts(i));
        data = get(obj, att);
        if isa(data, 'string') && verLessThan('matlab', '9.7')
            data = char(data); % Convert string attributes to character vectors instead to accommodate old version of MATLAB h5writeatt
        end
        if ~isempty(data)
            h5writeatt(h5filename, h5root, att, data);
        else
            delete(h5filename); % delete this incomplete file
            error(['Required attribute is not set! This file will not meet pradformat specs. Unset attribute: ' char(att) '. Please set a value and retry saving this file.'])
        end
    end

    % Write optional attributes to file
    for i=1:length(obj.opt_atts)
        att = char(obj.opt_atts(i));
        data = get(obj, att);
        if isa(data, 'string') && verLessThan('matlab', '9.7')
            data = char(data); % Convert string attributes to character vectors instead to accommodate old version of MATLAB h5writeatt
        end
        if ~isempty(data)
            h5writeatt(h5filename, h5root, att, data); 
        end
    end
end

