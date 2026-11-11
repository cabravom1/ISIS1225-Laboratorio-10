"""
TAD Grafo dirigido (digraph) implementado con listas de adyacencia.

El grafo se representa como un diccionario con dos llaves:

- ``vertices``: mapa (map_linear_probing) cuya llave es la llave del vertice
  y cuyo valor es el vertice (ver ``vertex.py``). Cada vertice guarda en
  ``adjacents`` un mapa con sus arcos salientes (ver ``edge.py``).
- ``num_edges``: numero de arcos del grafo.
"""

from DataStructures.Map import map_linear_probing as mp
from DataStructures.Graph import vertex as V
from DataStructures.Graph import edge as E


def new_graph(order):
    """
    Crea un grafo dirigido vacio.

    :param order: Numero estimado de vertices del grafo
    :type order: int

    :returns: Grafo recien creado
    :rtype: digraph
    """
    graph = {
        "vertices": mp.new_map(order, 0.5),
        "num_edges": 0,
    }
    return graph


def insert_vertex(my_graph, key_u, info_u):
    """
    Inserta el vertice ``key_u`` con la informacion ``info_u``.
    Si el vertice ya existe, se reemplaza por uno nuevo (sin arcos).

    :param my_graph: Grafo sobre el cual se inserta el vertice
    :param key_u: Llave del vertice
    :param info_u: Informacion asociada al vertice

    :returns: El grafo con el vertice insertado
    :rtype: digraph
    """
    vertex = V.new_vertex(key_u, info_u)
    my_graph["vertices"] = mp.put(my_graph["vertices"], key_u, vertex)
    return my_graph


def add_edge(my_graph, key_u, key_v, weight=1.0):
    """
    Agrega el arco dirigido ``key_u -> key_v`` con peso ``weight``.
    Si el arco ya existe, solo se actualiza su peso (no se cuenta dos veces).

    :param my_graph: Grafo al que se agrega el arco
    :param key_u: Llave del vertice de origen
    :param key_v: Llave del vertice de destino
    :param weight: Peso del arco

    :returns: El grafo con el arco agregado
    :rtype: digraph

    :raises Exception: Si alguno de los vertices no existe
    """
    vertex_u = mp.get(my_graph["vertices"], key_u)
    if vertex_u is None:
        raise Exception("El vertice u no existe")
    if mp.get(my_graph["vertices"], key_v) is None:
        raise Exception("El vertice v no existe")

    existing_edge = V.get_edge(vertex_u, key_v)
    if existing_edge is not None:
        E.set_weight(existing_edge, weight)
    else:
        V.add_adjacent(vertex_u, key_v, weight)
        my_graph["num_edges"] += 1
    return my_graph


def contains_vertex(my_graph, key_u):
    """
    Indica si el vertice ``key_u`` esta en el grafo.

    :returns: True si el vertice existe, False en caso contrario
    :rtype: bool
    """
    return mp.contains(my_graph["vertices"], key_u)


def order(my_graph):
    """
    Retorna el orden del grafo, es decir, el numero de vertices.

    :rtype: int
    """
    return mp.size(my_graph["vertices"])


def size(my_graph):
    """
    Retorna el tamaño del grafo, es decir, el numero de arcos.

    :rtype: int
    """
    return my_graph["num_edges"]
