class Grafo
  def initialize
    @adyacencias = {}
  end

  def agregar_arista(origen, destino)
    @adyacencias[origen] ||= []
    @adyacencias[origen] << destino
  end

  def vecinos(nodo)
    @adyacencias[nodo] || []
  end
end

class Busqueda
  def initialize(grafo)
    @grafo = grafo
  end

  def buscar(d, h)
    raise NotImplementedError, "Este método debe ser implementado por la subclase"
  end
end

class DFS < Busqueda
  def buscar(d, h)
    pila = [d]
    visitados = {}
    explorados = 0

    until pila.empty?
      nodo = pila.pop
      next if visitados[nodo]

      visitados[nodo] = true
      explorados += 1
      return explorados if nodo == h

      @grafo.vecinos(nodo).each { |vecino| pila.push(vecino) }
    end

    -1
  end
end

class BFS < Busqueda
  def buscar(d, h)
    cola = [d]
    visitados = {}
    explorados = 0

    until cola.empty?
      nodo = cola.shift
      next if visitados[nodo]

      visitados[nodo] = true
      explorados += 1
      return explorados if nodo == h

      @grafo.vecinos(nodo).each { |vecino| cola.push(vecino) }
    end

    -1
  end
end

# Ejemplo de uso
grafo = Grafo.new
grafo.agregar_arista(1, 2)
grafo.agregar_arista(1, 3)
grafo.agregar_arista(2, 4)

dfs = DFS.new(grafo)
puts dfs.buscar(1, 4) # 3

bfs = BFS.new(grafo)
puts bfs.buscar(1, 4) # 3
