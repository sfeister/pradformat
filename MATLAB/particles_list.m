classdef particles_list < matlab.mixin.SetGetExactNames & matlab.mixin.CustomDisplay
    % Particles List class
    properties (Constant)
        object_type = "particles";
        particles_type = "list";
    end
    properties
        x (:,:) {mustBeNumeric}
        y (:,:) {mustBeNumeric}
        z (:,:) {mustBeNumeric}
        px (:,:) {mustBeNumeric}
        py (:,:) {mustBeNumeric}
        pz (:,:) {mustBeNumeric}
        charge (:,:) {mustBeNumeric}
        mass (:,:) {mustBeNumeric}
        energy (:,:) {mustBeNumeric}
        weight (:,:) {mustBeNumeric}
        spec_name (:,:) string
        id (:,:) {mustBeNumeric}
        
        pradformat_version string = "0.1.0"
        shuffled {mustBeNonnegative, mustBeInteger}
        label string
        description string
        file_date string
        raw_data_filename string       
    end
    properties (Hidden)
        % Categorize the above public properties as required or optional
        req_ds = ["x", "y", "z", "px", "py", "pz", "charge", "mass"]; % Required datasets
        opt_ds = ["energy", "weight", "spec_name", "id"]; % Optional datasets
        req_atts = [...  % Required attributes
            "object_type", ...
            "particles_type", ...
            "pradformat_version", ...
            ];
        opt_atts = [...  % Optional attributes
            "shuffled", ...
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
            % Saves Particles List object to HDF5 file
            obj.validate();
            
            % Delete any existing file
            if isfile(h5filename)
                delete(h5filename);
            end
            
            % Create new file and save object into it
            save_prad_group(obj, h5filename, "/")
        end
    end
end
