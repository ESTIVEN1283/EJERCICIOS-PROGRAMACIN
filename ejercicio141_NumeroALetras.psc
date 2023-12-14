Algoritmo ejercicio141_NumeroALetras
    Definir num, unidad, decena, centena Como Entero;
    Definir resultado, unidadTxt, decenaTxt, centenaTxt Como Cadena;
	
    Escribir "Ingrese un número entre 1 y 1000: ";
    Leer num;
	
    // Validar que el número esté en el rango permitido
    Si num < 1 o num > 1000 Entonces
        Escribir "El número ingresado no está en el rango permitido.";
    Sino
        // Descomponer el número en unidades, decenas y centenas
        unidad <- num MOD 10;
        decena <- trunc(num / 10) MOD 10;
        centena <- trunc(num / 100) MOD 10;
		
        // Convertir las unidades a texto
        Segun unidad Hacer
            1: unidadTxt <- "uno";
            2: unidadTxt <- "dos";
            3: unidadTxt <- "tres";
            4: unidadTxt <- "cuatro";
            5: unidadTxt <- "cinco";
            6: unidadTxt <- "seis";
            7: unidadTxt <- "siete";
            8: unidadTxt <- "ocho";
            9: unidadTxt <- "nueve";
            De Otro Modo: unidadTxt <- "";
        FinSegun
		
        // Convertir las decenas a texto
        Segun decena Hacer
            1: 
                Segun unidad Hacer
                    0: decenaTxt <- "diez";
                    1: decenaTxt <- "once";
                    2: decenaTxt <- "doce";
                    3: decenaTxt <- "trece";
                    4: decenaTxt <- "catorce";
                    5: decenaTxt <- "quince";
                    De Otro Modo: decenaTxt <- "dieci" + unidadTxt;
                FinSegun
            2: decenaTxt <- "veinte";
            3: decenaTxt <- "treinta";
            4: decenaTxt <- "cuarenta";
            5: decenaTxt <- "cincuenta";
            6: decenaTxt <- "sesenta";
            7: decenaTxt <- "setenta";
            8: decenaTxt <- "ochenta";
            9: decenaTxt <- "noventa";
            De Otro Modo: decenaTxt <- "";
        FinSegun
		
        // Convertir las centenas a texto
        Segun centena Hacer
            1: centenaTxt <- "ciento";
            2: centenaTxt <- "doscientos";
            3: centenaTxt <- "trescientos";
            4: centenaTxt <- "cuatrocientos";
            5: centenaTxt <- "quinientos";
            6: centenaTxt <- "seiscientos";
            7: centenaTxt <- "setecientos";
            8: centenaTxt <- "ochocientos";
            9: centenaTxt <- "novecientos";
            De Otro Modo: centenaTxt <- "";
        FinSegun
		
        // Componer el resultado
        resultado <- centenaTxt + " " + decenaTxt + " " + unidadTxt;
        resultado <- (resultado);
        
        Escribir "El número ", num, " en palabras es: ", resultado;
    FinSi
FinAlgoritmo
