package huffman;


public class NodoArbol 
{
	private String simbolo;
	private int frecuencia;
	private NodoArbol izquierdo;
	private NodoArbol derecho;
	
	public NodoArbol(String simbolo, int frecuencia)
	{
		this.simbolo = simbolo;
		this.frecuencia = frecuencia;
		izquierdo=null;
		derecho=null;
	}
	
	public void InsertarNodo(DireccionNodo lado, NodoArbol nodo )
	{
		if (lado== DireccionNodo.Izquierdo)
		{
			izquierdo = nodo;
		}
		else
		{
			derecho = nodo;
		}
	}
	
	public int ObtenerFrecuencia()
	{
		return frecuencia;
	}
	
	public String ObtenerSimbolo()
	{
		return simbolo;
	}
	
	public NodoArbol ObtenerHijo(DireccionNodo lado)
	{
		if (lado == DireccionNodo.Izquierdo)
		{
			return izquierdo;
		}
		return derecho;
	}
	
}
