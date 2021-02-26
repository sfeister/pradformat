classdef Sensitivity < matlab.mixin.SetGetExactNames & matlab.mixin.CustomDisplay
    % Sensitivity class (for use with Advanced Radiograph objects)
    properties (Constant)
        group_type = "sensitivity";
    end
    properties
        energies(:,:) {mustBeNumeric}
        scale_factors(:,:,:) {mustBeNumeric}
        prescale_factors(:,:,:) {mustBeNumeric}
        
        spec_name string
        spec_mass double
        spec_charge double
    end
    properties (Hidden)
        % Categorize the above public properties as required or optional
        req_ds = ["energies", "scale_factors"]; % Required datasets
        opt_ds = ["prescale_factors"]; % Optional datasets
        req_atts = [...  % Required attributes
            "group_type", ...
            "spec_name", ...
            "spec_mass", ...
            "spec_charge", ...
            ];
        opt_atts = [];  % Optional attributes
        % List for a second time any above properties that are constants
        % of the class (and are not to be overwritten when reading from file)
        const_atts = ["group_type"];
    end
    methods (Access = protected)
       function propgrps = getPropertyGroups(obj)
          % Customized pretty printing of object
          propgrp1 = matlab.mixin.util.PropertyGroup(cellstr(obj.req_ds), 'Datasets (Required)');
          propgrp2 = matlab.mixin.util.PropertyGroup(cellstr(obj.opt_ds), 'Datasets (Optional)');
          propgrp3 = matlab.mixin.util.PropertyGroup(cellstr(obj.req_atts), 'Attributes (Required)');
          % propgrp4 = matlab.mixin.util.PropertyGroup(cellstr(obj.opt_atts), 'Attributes (Optional)');
          propgrps = [propgrp1 propgrp2 propgrp3];
       end
       function validate(obj)
            % Validate that all required properties have been set.
            % If some are not, throw an error.
            for i=1:length(obj.req_ds)
                ds = char(obj.req_ds(i));
                if isempty(get(obj, ds))
                    error(['Please assign a value to all required properties.' newline 'The following required dataset property is not yet assigned: "' char(ds) '".' newline 'Assign a value via "object.' char(ds) ' = value" and try again.'])
                end
            end           
            for i=1:length(obj.req_atts)
                att = char(obj.req_atts(i));
                if isempty(get(obj, att))
                    error(['Please assign a value to all required properties.' newline 'The following required attribute property is not yet assigned: "' char(att) '". ' newline 'Assign a value via "object.' char(att) ' = value" and try again.'])
                end
            end
       end
    end
end
