classdef SimpleInversion < matlab.mixin.SetGetExactNames & matlab.mixin.CustomDisplay
    % Simple Inversion class
    properties (Constant)
        object_type = "inversion";
        inversion_type = "simple";
    end
    properties
        phi(:,:) {mustBeNumeric}
        defl_ax1(:,:) {mustBeNumeric}
        defl_ax2(:,:) {mustBeNumeric}
        
        pradformat_version string = pradformat_version()
        dr double
        source_object_dist double
        object_image_dist double
        spec_name string
        spec_mass double
        spec_charge double
        spec_energy double
        dr_ax2 double
        source_radius double
        label string
        description string
        file_date string = datestr(datetime('now'), 'yyyy-mm-dd')
        radiograph_filename string       
        fields_filename string       
    end
    properties (Hidden)
        % Categorize the above public properties as required or optional
        req_ds = []; % Required datasets
        opt_ds = ["phi", "defl_ax1", "defl_ax2"]; % Optional datasets
        req_atts = [...  % Required attributes
            "object_type", ...
            "inversion_type", ...
            "pradformat_version", ...
            "dr", ...
            "source_object_dist", ...
            "object_image_dist", ...
            "spec_name", ...
            "spec_mass", ...
            "spec_charge", ...
            "spec_energy", ...
            ];
        opt_atts = [...  % Optional attributes
            "dr_ax2", ...
            "source_radius", ...
            "label", ...
            "description", ...
            "file_date", ...
            "radiograph_filename", ...
            "fields_filename", ...
            ];
        % List for a second time any above properties that are constants
        % of the class (and are not to be overwritten when reading from file)
        const_atts = ["object_type", "inversion_type"]
    end
    methods (Access = protected)
       function propgrps = getPropertyGroups(obj)
          % Customized pretty printing of object
          % propgrp1 = matlab.mixin.util.PropertyGroup(cellstr(obj.req_ds), 'Datasets (Required)');
          propgrp2 = matlab.mixin.util.PropertyGroup(cellstr(obj.opt_ds), 'Datasets (Optional)');
          propgrp3 = matlab.mixin.util.PropertyGroup(cellstr(obj.req_atts), 'Attributes (Required)');
          propgrp4 = matlab.mixin.util.PropertyGroup(cellstr(obj.opt_atts), 'Attributes (Optional)');
          propgrps = [propgrp2 propgrp3 propgrp4];
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
    methods
        function obj = SimpleInversion(h5filename)
            % Constructor method - load object from file
            if nargin == 1
                % Load in the prad object from h5filename
                load_prad_group(obj, h5filename, '/')
            end
        end
        function prad_save(obj, h5filename)
            % Saves Simple Radiograph object to HDF5 file
            obj.validate();
            
            % Delete any existing file
            if (exist(h5filename, 'file') == 2)
                delete(h5filename);
                if (exist(h5filename, 'file') == 2)
                    error(['The existing HDF5 file: "' h5filename '" could not be overwritten.' newline 'Perhaps you do not have permissions to delete this file.' newline 'For example, perhaps the file is open and being read by another program, like HDFView? If so, close the file in that program.' newline 'Or, perhaps this file handle is currently open in MATLAB? Try the command fclose(''all'') to close all current file handles.' newline 'If all else fails, try manually deleting the file in question, or change your desired output filename to something else.' newline 'Once you''re done troubleshooting, run your script again.']);
                end
            end
            
            % Create new file and save object into it
            save_prad_group(obj, h5filename, '/')
        end
    end
end
