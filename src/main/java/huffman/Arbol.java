package huffman;

import java.util.Hashtable;

public class Arbol 
{
	public NodoArbol raiz;
	
	public Arbol(String simbolo, int frecuencia)
	{
		raiz = new NodoArbol(simbolo, frecuencia);
	}
	
	public Arbol(Arbol izquierdo, Arbol derecho)
	{
		int frecuencia = izquierdo.ObtenerRaiz().ObtenerFrecuencia() + derecho.ObtenerRaiz().ObtenerFrecuencia();
		raiz = new NodoArbol(null, frecuencia);
		raiz.InsertarNodo(DireccionNodo.Izquierdo, izquierdo.ObtenerRaiz());
		raiz.InsertarNodo(DireccionNodo.Derecho, derecho.ObtenerRaiz());
	}
	
	private NodoArbol ObtenerRaiz()
	{
		return raiz;
	}
	
	public int ObtenerFrecuencia()
	{
		return raiz.ObtenerFrecuencia();
	}
	
	public Hashtable<String,String> CalcularCodigoHuffman()
	{
		Hashtable<String,String> tablaCodigoHuffman = new Hashtable<String,String>();
		PreOrden(this.raiz, "", tablaCodigoHuffman);
		return tablaCodigoHuffman;
	}
	private void PreOrden(NodoArbol raiz, String codigoHuffman, Hashtable<String,String> tablaCodigoHuffman)
	{
		NodoArbol izquierdo = raiz.ObtenerHijo(DireccionNodo.Izquierdo);
		if( izquierdo != null)
		{
			PreOrden(izquierdo, codigoHuffman+"0", tablaCodigoHuffman);
		}
		
		NodoArbol derecho = raiz.ObtenerHijo(DireccionNodo.Derecho);
		if(derecho != null)
		{
			PreOrden(derecho, codigoHuffman+"1", tablaCodigoHuffman);
		}
		
		if (izquierdo == null && derecho==null)
		{
			System.out.println(raiz.ObtenerSimbolo() + ":"+codigoHuffman);
			tablaCodigoHuffman.put(raiz.ObtenerSimbolo(), codigoHuffman);
		}
	}
}
