package analizador_main;

import analizador.*;
import java.io.FileInputStream;
import java.io.InputStream;
import java.io.FileNotFoundException;

/**
 *
 * @author Mario Pineda
 */
public class Analizador_sintactico {

    public static void main(String[] args) {
        // Ruta del archivo a analizar
        String filePath = "./arch_prueba.js";
        //String filePath = "./arch_prueba2.js";
        //String filePath = "./arch_prueba_vacio.js";

        try {
            // Abre un flujo de entrada desde el archivo especificado
            InputStream inputStream = new FileInputStream(filePath);
            
            // Crea una instancia del analizador y le pasa el flujo de entrada
            JavaScriptLexer parser = new JavaScriptLexer(inputStream);

            try {
                // Intenta analizar el archivo como un programa válido
                parser.Program();
                System.out.println("La sintaxis del archivo es correcta.");
            } catch (ParseException e) {
                // Si se lanza una ParseException, la sintaxis es incorrecta
                System.out.println("Error de sintaxis en el archivo: " + e.getMessage());
            }

        } catch (FileNotFoundException e) {
            // Si el archivo no se encuentra, se maneja esta excepción
            System.out.println("El archivo no se encontró");
        }
    }

}
