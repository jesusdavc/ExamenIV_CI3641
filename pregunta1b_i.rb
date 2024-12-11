class Secuencia
    def agregar(elemento)
        raise NotImplementedError, "Este método debe ser implementado por la subclase"
    end

    def remover
        raise NotImplementedError, "Este método debe ser implementado por la subclase"
    end

    def vacio
        raise NotImplementedError, "Este método debe ser implementado por la subclase"
    end
end

class Pila < Secuencia
    def initialize
        @elementos = []
    end

    def agregar(elemento)
        @elementos.push(elemento)
    end

    def remover
        raise "Pila vacía" if vacio
        @elementos.pop
    end

    def vacio
        @elementos.empty?
    end
end

class Cola < Secuencia
    def initialize
        @elementos = []
    end

    def agregar(elemento)
        @elementos.push(elemento)
    end

    def remover
        raise "Cola vacía" if vacio
        @elementos.shift
    end

    def vacio
        @elementos.empty?
    end
end

# Ejemplo de uso
pila = Pila.new
pila.agregar(1)
pila.agregar(2)
puts pila
puts pila.remover # 2

cola = Cola.new
cola.agregar(1)
cola.agregar(2)
puts cola
puts cola.remover # 1
