//package analyzer;
//
///**
// *
// * @author Mario
// */
//public class Analizador_sintactico {
//    public static void main(String[] args) {
//        System.out.println("Si jaló wey");
//    }
//}

package analyzer;

import Analizador.Gramatica;
import Analizador.ParseException;
import Analizador.TokenMgrError;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.logging.Level;
import java.util.logging.Logger;
/**
 *
 * @author Mario Pineda
 */
public class Analizador_sintactico {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        try {
            Gramatica parser = new Gramatica(new BufferedReader(new FileReader("./pruebas.txt")));
            parser.Analizar();
        } catch (ParseException e) {
            System.err.println(e.getMessage());
        } catch (FileNotFoundException e) {
            Logger.getLogger(Analizador_sintactico.class.getName()).log(Level.SEVERE, "Error al intentar leer el archivo.", e);
        } catch(TokenMgrError e){
            System.err.println(e.getMessage());
        }
    }
    
}