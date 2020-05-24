package huffman;

import java.util.ArrayList;
import java.util.BitSet;
import java.util.Collections;
import java.util.Comparator;
import java.util.Enumeration;
import java.util.HashMap;
import java.util.Hashtable;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;


public class Huffman 
{
	static final int LONGITUD_CARACTER_BITS = 8; // Se usan 8 bits para codificar y decodificar el mensaje.
	public Hashtable<String,String> tablaCodigoHuffman;
	String finCadena = Character.toString ((char) 36); //Caracter fin de texto
	
	public Huffman()
	{
		
	}
	
	public byte[] Comprimir(String cadena)
	{
		/*
		 * Primer paso: Determinar los caracteres que aparecen, y calcular la frecuencia.
		 * Una vez hecho esto se deben ordenar los caracteres de menor a mayor frecuencia
		 */
		
		cadena += finCadena;
		Hashtable<String,Integer> tablaFrecuencias = new Hashtable<String,Integer>();
		for (int i=0; i<cadena.length(); i++)
		{
			String caracter = cadena.substring(i, i+1);
			Integer n = tablaFrecuencias.get(caracter);
			if (n!= null)
			{
				tablaFrecuencias.put(caracter, n+1);
			}
			else
			{
				tablaFrecuencias.put(caracter, 1);
			}
		}
		List<Entry<String, Integer>> listEntry = OrdenarTablaFrecuencias(tablaFrecuencias);
		
		
		/*
		 * Es necesario convertir los elementos de la lista ordenada en lista de arboles. 
		 */
		
		ArrayList<Arbol> listaArbol = ObtenerListaArboles(listEntry);
		/*for(Arbol arbol: listaArbol)
		{
			System.out.println(arbol.raiz.ObtenerSimbolo()+":"+arbol.ObtenerFrecuencia());
		}
		*/
		
		
		/*
		 * Segundo Paso: Construir un árbol binario, a partir de los dos primeros elementos de la lista de arboles.
		 * El árbol resultante se agrega a la lista en orden de su frecuencia.
		 * Este paso se repite hasta que la lista contenga solamente un elemento. 
		 */
		
		while(listaArbol.size() >= 2)
		{
			Arbol izquierdo = listaArbol.get(0);
			Arbol derecho = listaArbol.get(1);
			listaArbol.remove(0);
			listaArbol.remove(0);
			
			Arbol nuevoArbol = new Arbol(izquierdo, derecho);
			
			//Insertar nuevoArbol en el lugar adecuado:
			//	obtener la frecuencia de todo el arbol, e insertar el arbol en la lista justo antes del elemento de mayor frecuencia
			//	Se puede requerir insertarlo al inicio o al final.
			
			int frecuencia = nuevoArbol.ObtenerFrecuencia();
			int i = 0;
			boolean insertado = false;
			for(Arbol arbol: listaArbol)
			{
				if(arbol.ObtenerFrecuencia() > frecuencia)
				{
					listaArbol.add(i, nuevoArbol);
					insertado = true;
					break;
				}
				i++;
			}
			if(!insertado)
			{
				listaArbol.add(nuevoArbol);
			}
			
		}
		
		tablaCodigoHuffman = listaArbol.get(0).CalcularCodigoHuffman();
		
		//Tecnicamente, en este punto, el algoritmo de Huffman ya ha terminado. El sisguiente paso
		//es poder convertir la cadena original en una nueva cadena comprimida. A este proceso le 
		//llamaremos codificación.
		
		return Codificar(tablaCodigoHuffman, cadena);
		
		
	}
	
	private byte[] Codificar(Hashtable<String,String> tablaCodigoHuffman, String cadena)
	{
		//Convertir texto original en una versión comprimida, dada por la tabla de codificación,
		//la cual fue obtenida mediante el algoritmo de Huffman
		
		String cadenaBinaria="";
		int numBit=0;
		for(int i=0; i<cadena.length(); i++)
		{
			String codigo = tablaCodigoHuffman.get( cadena.substring(i,i+1) );
			for (int j=0; j < codigo.length(); j++)
			{
				if( codigo.substring(j, j+1).equals("1") )
				{
					cadenaBinaria+="1";
				}
				else
				{
					cadenaBinaria+="0";
				}
				numBit++;
			}
		}
		
		int numCaracteresFinal =(int) Math.ceil(numBit / LONGITUD_CARACTER_BITS);
		byte[] cadenaCodificada = new byte[numCaracteresFinal];
		
		int desdeIndex = 0;
		int hastaIndex = 0;
		for(int i=0; i<numCaracteresFinal; i++)
		{
			if ( (i+1) * LONGITUD_CARACTER_BITS < numBit )
			{
				desdeIndex = i * LONGITUD_CARACTER_BITS;
				hastaIndex = ((i+1)* LONGITUD_CARACTER_BITS );
			}
			else
			{
				desdeIndex += LONGITUD_CARACTER_BITS;
				hastaIndex += LONGITUD_CARACTER_BITS;
			}
			
			String nuevoByte = cadenaBinaria.substring( desdeIndex, hastaIndex );
			cadenaCodificada[i] = StringBitsAByte(nuevoByte);
		}
		return cadenaCodificada;
	}
	
	private byte StringBitsAByte(String nuevoByte)
	{
		byte suma=0;
		if (nuevoByte.length() == LONGITUD_CARACTER_BITS)
		{
			for (int i=LONGITUD_CARACTER_BITS-1; i>=0; i--)
			{
				suma +=(byte) (Integer.parseInt( nuevoByte.substring(i, i+1) ) * Math.pow(2, i ));
				int l=0;
			}
		}
		return suma;
	}
	
	
	private ArrayList<Arbol> ObtenerListaArboles(List<Entry<String, Integer>> listEntry)
	{
		ArrayList<Arbol> listaArbol = new ArrayList<Arbol>();
		for(Map.Entry<String, Integer> entry:listEntry)
		{
			Arbol temp = new Arbol(entry.getKey(), entry.getValue());
			listaArbol.add(temp);
		}
		return listaArbol;
	}
	
	private List<Entry<String, Integer>> OrdenarTablaFrecuencias(Hashtable<String,Integer> tablaFrecuencias)
	{
		Map<String, Integer> map = new HashMap<String, Integer>(tablaFrecuencias);
		Set<Entry<String, Integer>> set = map.entrySet();
		List<Entry<String, Integer>> list = new ArrayList<Entry<String, Integer>>(set);
		Collections.sort( list, 
				new Comparator<Map.Entry<String, Integer>>()
				{
					public int compare( Map.Entry<String, Integer> o1, Map.Entry<String, Integer> o2 )
					{
						return (o1.getValue()).compareTo( o2.getValue() );
					}
				} 
		);
		
		return list;
	}
	
	
	public String Descomprimir(byte[] cadenaCodificada, Hashtable<String,String> tablaCodigoHuffman)
	{
		String cadenaEnBinario = "";
		for (int i=0; i < cadenaCodificada.length; i++)
		{
			byte c = cadenaCodificada[i];
			cadenaEnBinario += String.format("%8s", Integer.toBinaryString(c & 0xFF)).replace(' ', '0');
		}
		//System.out.println(cadenaEnBinario);
		return Decodificar(cadenaEnBinario, InvertirTablaHash(tablaCodigoHuffman));
	}
	
	private String Decodificar(String cadenaEnBinario, Hashtable<String,String> tablaCodigoHuffman)
	{
		Enumeration<String> keys = tablaCodigoHuffman.keys();
		int maxLongitudCodigo = 0;
		String cadenaDecodificada="";
		
		while(keys.hasMoreElements())
		{
			String key1= keys.nextElement();
			int dim = key1.length();
			if( dim > maxLongitudCodigo)
				maxLongitudCodigo = dim;
		}
		
		String ultimoCaracter="";
		while(ultimoCaracter != finCadena)
		{
			String codigo = "";
			for (int i=0; i<maxLongitudCodigo;  i++)
			{
				codigo = cadenaEnBinario.substring(0, i+1);
				if ( tablaCodigoHuffman.containsKey(codigo) )
				{
					ultimoCaracter = tablaCodigoHuffman.get(codigo);
					if (ultimoCaracter != finCadena)
						cadenaDecodificada += ultimoCaracter;
					if ( (i+1) < cadenaEnBinario.length() )
						cadenaEnBinario = cadenaEnBinario.substring(i+1, cadenaEnBinario.length());
					break;
				}
			}
		}
		
		return cadenaDecodificada;
	}	
	
	private Hashtable<String,String> InvertirTablaHash(Hashtable<String,String> tablaCodigoHuffman)
	{
		Hashtable<String,String> nuevaTabla = new Hashtable<String,String>();
		Enumeration<String> keys =tablaCodigoHuffman.keys();
		while(keys.hasMoreElements())
		{
			String llaveActual = keys.nextElement();
			nuevaTabla.put(tablaCodigoHuffman.get(llaveActual), llaveActual);
		}
		
		
		return nuevaTabla;
	}
	
}








/*
 * Recorrer un hashtable
Enumeration<String> llaves = tablaFrecuencias.keys();
while (llaves.hasMoreElements()) 
{
	String c =llaves.nextElement();
	System.out.println(""+"hashtable elementos: " + c + ":"+tablaFrecuencias.get(c));
}
*/

/*
Recorrer un List<Entry<String, Integer>>, y acceder a key y value
for(Map.Entry<String, Integer> entry:list)
{
	System.out.println(entry.getKey()+" ==== "+entry.getValue());
	
}
		
*/