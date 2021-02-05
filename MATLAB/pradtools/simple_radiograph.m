classdef simple_radiograph
    % Simple Radiograph class
    properties (Constant)
        object_type = "radiograph";
        radiograph_type = "simple";
    end
    properties
        image
        X
        Y
        Z
        pradtools_version = "0.0.0"
        pixel_width
        scale_factor
        source_distance
        ROI_distance
        spec_name
        spec_mass
        spec_charge
        spec_energy
    end
    methods
        function prad_save(obj, h5filename)
            % Saves monochromatic radiograph to HDF5 file
            if isfile(h5filename)
                delete(h5filename); % truncate current file
            end
            if ~isempty(obj.image)
                h5create(h5filename, '/image', size(obj.image))
                h5write(h5filename, '/image', obj.image)
            end
            if ~isempty(obj.X)
                h5create(h5filename,'/X', size(obj.X))
                h5write(h5filename,'/X', obj.X)
            end
            if ~isempty(obj.Y)
                h5create(h5filename,'/Y', size(obj.Y))
                h5write(h5filename,'/Y', obj.Y)
            end
            if ~isempty(obj.Z)
                h5create(h5filename,'/Z', size(obj.Z))
                h5write(h5filename,'/Z', obj.Z)
            end
            if ~isempty(obj.object_type)
                h5writeatt(h5filename, '/', 'object_type', obj.object_type)
            end
            if ~isempty(obj.radiograph_type)
                h5writeatt(h5filename, '/', 'radiograph_type', obj.radiograph_type)
            end
            if ~isempty(obj.pradtools_version)
                h5writeatt(h5filename, '/', 'pradtools_version', obj.pradtools_version)
            end
            if ~isempty(obj.pixel_width)
                h5writeatt(h5filename, '/', 'pixel_width', obj.pixel_width)
            end
            if ~isempty(obj.scale_factor)
                h5writeatt(h5filename, '/', 'scale_factor', obj.scale_factor)
            end
            if ~isempty(obj.source_distance)
                h5writeatt(h5filename, '/', 'source_distance', obj.source_distance)
            end
            if ~isempty(obj.ROI_distance)
                h5writeatt(h5filename, '/', 'ROI_distance', obj.ROI_distance)
            end
            if ~isempty(obj.spec_name)
                h5writeatt(h5filename, '/', 'spec_name', obj.spec_name)
            end
            if ~isempty(obj.spec_mass)
                h5writeatt(h5filename, '/', 'spec_mass', obj.spec_mass)
            end
            if ~isempty(obj.spec_charge)
                h5writeatt(h5filename, '/', 'spec_charge', obj.spec_charge)
            end
            if ~isempty(obj.spec_energy)
                h5writeatt(h5filename, '/', 'spec_energy', obj.spec_energy)
            end
        end
    end
end
