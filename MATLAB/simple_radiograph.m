classdef simple_radiograph < matlab.mixin.SetGetExactNames & matlab.mixin.CustomDisplay
    % Simple Radiograph class
    properties (Constant)
        object_type = "radiograph";
        radiograph_type = "simple";
    end
    properties
        image(:,:) {mustBeNumeric}
        X(:,:) {mustBeNumeric}
        Y(:,:) {mustBeNumeric}
        T(:,:) double
        pradtools_version string = "0.0.0"
        scale_factor double
        pixel_width double
        pixel_width_ax2 double
        source_distance double
        ROI_distance double
        spec_name string
        spec_mass double
        spec_charge double
        spec_energy double
        label string
        description string
        experiment_date string
        file_date string
        raw_data_filename string       
    end
    properties (Constant)
        % Categorize the above public properties as required or optional
        req_ds = ["image"]; % Required datasets
        opt_ds = ["X", "Y", "T"]; % Optional datasets
        req_atts = [...  % Required attributes
            "object_type", ...
            "radiograph_type", ...
            "pradtools_version", ...
            "scale_factor", ...
            "pixel_width", ...
            ];
        opt_atts = [...  % Optional attributes
            "pixel_width_ax2", ...
            "source_distance", ...
            "ROI_distance", ...
            "spec_name", ...
            "spec_mass", ...
            "spec_charge", ...
            "spec_energy", ...
            "label", ...
            "description", ...
            "experiment_date", ...
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
            % Saves simple radiograph to HDF5 file
            obj.validate(); % Throw an error if any required properties are missing
            
            % Create file
            if isfile(h5filename)
                delete(h5filename); % truncate current file
            end
            
            % Write required datasets to file (%TODO: Add chunking and compression?)
            if ~isempty(obj.image)
                h5create(h5filename, '/image', size(obj.image))
                h5write(h5filename, '/image', obj.image)
            end
            
            % Write optional datasets to file
            if ~isempty(obj.X)
                h5create(h5filename,'/X', size(obj.X))
                h5write(h5filename,'/X', obj.X)
            end
            if ~isempty(obj.Y)
                h5create(h5filename,'/Y', size(obj.Y))
                h5write(h5filename,'/Y', obj.Y)
            end
            if ~isempty(obj.T)
                h5create(h5filename,'/T', size(obj.T))
                h5write(h5filename,'/T', obj.T)
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
