package prTableToXML.IS;

import java.util.List;
import java.io.*;
import java.util.LinkedList;

public class archivo {
	 
	private String nomFich;
	
	public archivo(String nom){
		nomFich=nom;
	}
	
    public void escribir(List<String> hist)
    {
       	
        FileWriter fichero = null;
        PrintWriter pw = null;
        

        try
        {
        	fichero = new FileWriter(nomFich);
           	pw = new PrintWriter(fichero); 
        	
        	for(String h : hist)
           		pw.println(h);
        
        } catch (Exception e) {
        	e.printStackTrace();
        } finally {
        	try {
    			// Nuevamente aprovechamos el finally para 
        		// asegurarnos que se cierra el fichero.
        		if (null != fichero)
        			fichero.close();
        			//pw.close();
        	} catch (Exception e2) {
        		e2.printStackTrace();
        	}
        }
    	
    }
 
    public List<String> leer()
    {
        File archivo = null;
        FileReader fr = null;
        BufferedReader br = null;
        List<String> hist= new LinkedList<String>();
        
        try {
			// Apertura del fichero y creacion de BufferedReader para poder
			// hacer una lectura comoda (disponer del metodo readLine()).
			archivo = new File (nomFich);
			fr = new FileReader (archivo);
			br = new BufferedReader(fr);
 
			// Lectura del fichero
			String linea;
			while((linea=br.readLine())!=null)
				hist.add(linea);
        }
        catch(Exception e){
           e.printStackTrace();
        }finally{
           // En el finally cerramos el fichero, para asegurarnos
           // que se cierra tanto si todo va bien como si salta 
           // una excepcion.
           try{
              if( null != fr ){
                 fr.close();
              }
           }catch (Exception e2){
              e2.printStackTrace();
           }
        }
        if(hist.size()==0)
        	return null;
        else
        	return hist;
    }
}