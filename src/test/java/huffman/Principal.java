package huffman;

import huffman.Huffman;

public class Principal {

	public static void main(String[] args)
	{
		
		// TODO Auto-generated method stub
		Huffman hf = new Huffman();
		//hf.Comprimir("ESTO ES UN EJEMPLO DE UN ARBOL DE HUFFMAN");
		//hf.Comprimir("HOLA MAMA");
		//hf.Comprimir("");
		//byte[] cadenaCodificada = hf.Comprimir("j'aime aller sur le bord de l'eau les jeudis ou les jours impairs");
		byte[] cadenaCodificada = hf.Comprimir("HOLA MAMA");
		
		
		//System.out.println( hf.Descomprimir( cadenaCodificada, hf.tablaCodigoHuffman ) );
	}

}
