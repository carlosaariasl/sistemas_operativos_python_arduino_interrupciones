// Definir pines para LEDs y pushbuttons
const int ledVerde = 2;
const int ledRojo = 3;
const int ledAmarillo = 4;
const int btnVerde = 5;
const int btnRojo = 6;
const int btnAmarillo = 7;

void setup() {
  // Configurar pines de LEDs como salidas
  pinMode(ledVerde, OUTPUT);
  pinMode(ledRojo, OUTPUT);
  pinMode(ledAmarillo, OUTPUT);
  // Configurar pines de pushbuttons como entradas con pull-up
  pinMode(btnVerde, INPUT_PULLUP);
  pinMode(btnRojo, INPUT_PULLUP);
  pinMode(btnAmarillo, INPUT_PULLUP);
  // Adjuntar interrupciones a los pines de los pushbuttons
  attachInterrupt(digitalPinToInterrupt(btnVerde), verdeInterrupt, FALLING);
  attachInterrupt(digitalPinToInterrupt(btnRojo), rojoInterrupt, FALLING);
  attachInterrupt(digitalPinToInterrupt(btnAmarillo), amarilloInterrupt, FALLING);
}

void loop() {
  // No es necesario escribir código en el loop para este ejemplo
}

// Funciones de interrupción para cada pushbutton
void verdeInterrupt() {
  digitalWrite(ledVerde, !digitalRead(ledVerde)); // Alternar el estado del LED verde
}

void rojoInterrupt() {
  digitalWrite(ledRojo, !digitalRead(ledRojo)); // Alternar el estado del LED rojo
}

void amarilloInterrupt() {
  digitalWrite(ledAmarillo, !digitalRead(ledAmarillo)); // Alternar el estado del LED amarillo
}
