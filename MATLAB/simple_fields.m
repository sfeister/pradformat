classdef simple_fields
    % Simple Fields class
    properties (Constant)
        object_type = "fields";
        fields_type = "simple";
    end
    properties
        X
        Y
        Z
        Ex
        Ey
        Ez
        Bx
        By
        Bz
        pradtools_version = "0.0.0"
    end
    methods
        function prad_save(obj, h5filename)
            % Saves fields object to HDF5 file
            % TODO: Add compression to the HDF5 file output, including auto-chunking
            % and setting data type I suppose!

            if isfile(h5filename)
                delete(h5filename); % truncate current file
            end
            if ~isempty(obj.X)
                h5create(h5filename, '/X', size(obj.X))
                h5write(h5filename, '/X', obj.X)
            end
            if ~isempty(obj.Y)
                h5create(h5filename, '/Y', size(obj.Y))
                h5write(h5filename, '/Y', obj.Y)
            end
            if ~isempty(obj.Z)
                h5create(h5filename, '/Z', size(obj.Z))
                h5write(h5filename, '/Z', obj.Z)
            end
            if ~isempty(obj.Ex)
                h5create(h5filename, '/Ex', size(obj.Ex))
                h5write(h5filename, '/Ex', obj.Ex)
            end
            if ~isempty(obj.Ey)
                h5create(h5filename, '/Ey', size(obj.Ey))
                h5write(h5filename, '/Ey', obj.Ey)
            end
            if ~isempty(obj.Ez)
                h5create(h5filename, '/Ez', size(obj.Ez))
                h5write(h5filename, '/Ez', obj.Ez)
            end
            if ~isempty(obj.Bx)
                h5create(h5filename, '/Bx', size(obj.Bx))
                h5write(h5filename, '/Bx', obj.Bx)
            end
            if ~isempty(obj.By)
                h5create(h5filename, '/By', size(obj.By))
                h5write(h5filename, '/By', obj.By)
            end
            if ~isempty(obj.Bz)
                h5create(h5filename, '/Bz', size(obj.Bz))
                h5write(h5filename, '/Bz', obj.Bz)
            end
            if ~isempty(obj.object_type)
                h5writeatt(h5filename, '/', 'object_type', obj.object_type)
            end
            if ~isempty(obj.fields_type)
                h5writeatt(h5filename, '/', 'fields_type', obj.fields_type)
            end
            if ~isempty(obj.pradtools_version)
                h5writeatt(h5filename, '/', 'pradtools_version', obj.pradtools_version)
            end
        end
    end
end
