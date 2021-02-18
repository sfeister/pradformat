function [] = load_prad_group(obj, h5filename, h5root)
%LOAD_PRAD_GROUP Load all optional/required group-level datasets/attributes (specified in a prad object) from an
%already-created group in an existing HDF5 file into that prad object
%   h5root should be something like "/" or "/mygrp/", and must end with a
%   forwardslash
    
    % Enforce h5root as char array and last character of h5root being a forward-slash
    h5root = char(h5root);
    if ~strcmp(h5root(end),  '/')
        h5root = strcat(h5root, '/');
    end

    % Read in required datasets
    for i=1:length(obj.req_ds)
        ds = obj.req_ds(i);
        try
            data = h5read(h5filename, [h5root char(ds)]);
            set(obj, ds, data);
        catch
            warning(['Failed to read in required dataset "' char(ds) '". Could it be missing from this file?'])
        end
    end

    % Read in optional datasets
    for i=1:length(obj.opt_ds)
        ds = obj.opt_ds(i);
        try
            data = h5read(h5filename, [h5root char(ds)]);
            set(obj, ds, data);
        catch
        end
    end

    % Read in required attributes
    for i=1:length(obj.req_atts)
        att = obj.req_atts(i);
        if ~any(strcmp(att, obj.const_atts)) % These are fixed, set by the class definition; don't try to set these.
            try
                data = h5readatt(h5filename, h5root, att);
                set(obj, att, data);
            catch
                warning(['Failed to read in required attribute "' char(att) '". Could it be missing from this file?'])
            end
        end
    end

    % Read in optional attributes
    for i=1:length(obj.opt_atts)
        att = obj.opt_atts(i);
        try
            data = h5readatt(h5filename, h5root, att);
            set(obj, att, data);
        catch
        end
    end
end

