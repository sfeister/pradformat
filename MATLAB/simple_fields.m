classdef simple_fields < matlab.mixin.SetGetExactNames & matlab.mixin.CustomDisplay
    % Simple Fields class
    properties (Constant)
        object_type = "fields";
        fields_type = "simple";
    end
    properties
        X (:,:,:) {mustBeNumeric}
        Y (:,:,:) {mustBeNumeric}
        Z (:,:,:) {mustBeNumeric}
        Ex (:,:,:) {mustBeNumeric}
        Ey (:,:,:) {mustBeNumeric}
        Ez (:,:,:) {mustBeNumeric}
        Bx (:,:,:) {mustBeNumeric}
        By (:,:,:) {mustBeNumeric}
        Bz (:,:,:) {mustBeNumeric}
        rho (:,:,:) {mustBeNumeric}
        pradtools_version string = "0.0.0"
        rho_description string
        label string
        description string
        file_date string
        raw_data_filename string       
    end
    properties (Constant)
        % Categorize the above public properties as required or optional
        req_ds = ["X", "Y", "Z", "Ex", "Ey", "Ez", "Bx", "By", "Bz"]; % Required datasets
        opt_ds = ["rho"]; % Optional datasets
        req_atts = [...  % Required attributes
            "object_type", ...
            "fields_type", ...
            "pradtools_version", ...
            ];
        opt_atts = [...  % Optional attributes
            "rho_description", ...
            "label", ...
            "description", ...
            "file_date", ...
            "raw_data_filename", ...
            ];
    end
    methods (Access = protected)
       function propgrps = getPropertyGroups(obj)
          % Customized pretty printing of object
          propgrp1 = matlab.mixin.util.PropertyGroup(cellstr(obj.req_ds), 'Datasets (Required)');
          propgrp2 = matlab.mixin.util.PropertyGroup(cellstr(obj.opt_ds), 'Datasets (Optional)');
          propgrp3 = matlab.mixin.util.PropertyGroup(cellstr(obj.req_atts), 'Attributes (Required)');
          propgrp4 = matlab.mixin.util.PropertyGroup(cellstr(obj.opt_atts), 'Attributes (Optional)');
          propgrps = [propgrp1 propgrp2 propgrp3 propgrp4];
       end
       function validate(obj)
            % Validate that all required properties have been set.
            % If some are not, throw an error.
            for i=1:length(obj.req_ds)
                ds = obj.req_ds(i);
                if isempty(get(obj, ds))
                    error(['Please assign a value to all required properties.' newline 'The following required dataset property is not yet assigned: "' char(ds) '".' newline 'Assign a value via "object.' char(ds) ' = value" and try again.'])
                end
            end           
            for i=1:length(obj.req_atts)
                att = obj.req_atts(i);
                if isempty(get(obj, att))
                    error(['Please assign a value to all required properties.' newline 'The following required attribute property is not yet assigned: "' char(att) '". ' newline 'Assign a value via "object.' char(att) ' = value" and try again.'])
                end
            end
       end
    end
    methods
        function prad_save(obj, h5filename)
            % Saves simple fields to HDF5 file
            obj.validate(); % Throw an error if any required properties are missing
            
            % Create file
            if isfile(h5filename)
                delete(h5filename); % truncate current file
            end
            
            % Write required datasets to file % TODO: Force a certain array
            % size
            for i=1:length(obj.req_ds) %TODO: Add chunking and compression?)
                ds = obj.req_ds(i);
                data = get(obj, ds);
                h5create(h5filename, ['/' char(ds)], size(data));
                h5write(h5filename, ['/' char(ds)], data);
            end
            
            % Write optional datasets to file
            for i=1:length(obj.opt_ds) %TODO: Add chunking and compression?)
                ds = obj.opt_ds(i);
                data = get(obj, ds);
                if ~isempty(data)
                    h5create(h5filename, ['/' char(ds)], size(data));
                    h5write(h5filename, ['/' char(ds)], data);
                end
            end
            
            % Write required attributes to file
            for i=1:length(obj.req_atts)
                att = obj.req_atts(i);
                h5writeatt(h5filename, '/', att, get(obj, att));
            end

            % Write optional attributes to file
            for i=1:length(obj.opt_atts)
                att = obj.opt_atts(i);
                if ~isempty(get(obj, att))
                    h5writeatt(h5filename, '/', att, get(obj, att));
                end
            end
        end
    end
end
