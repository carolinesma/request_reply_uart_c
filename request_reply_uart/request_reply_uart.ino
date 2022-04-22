#include <stdio.h>
#include <stdlib.h>
#include <avr/interrupt.h>
#include <util/delay.h> 

void UART_Init(unsigned int ubrr);
void UART_Transmit(char *data);
unsigned char UART_Receive(void );
int main(void );

#define FOSC 1843200 // Clock Speed
#define BAUD 9600
#define MYUBRR FOSC/16/BAUD-1



void UART_Init( unsigned int ubrr)
{
  /*Set baud rate */
  UBRR0H = (unsigned char)(ubrr>>8);
  UBRR0L = (unsigned char)ubrr;
  /*Disable double speed*/
  UCSR0A = 0;
  /*Enable receiver and transmitter */
  UCSR0B = (1<<RXEN0)|(1<<TXEN0);
  /* Set frame format: 8data, 1 stop bit, none parity */
  UCSR0C = (0<<USBS0)|(1<<UCSZ01)|(1<<UCSZ00);
}

void UART_Transmit(unsigned char data)
{
  /* Wait for empty transmit buffer */
  while (!(UCSR0A & (1<<UDRE0)))
    ;
  /* Put data into buffer, sends the data */
  UDR0 = data;
}

unsigned char USART_Receive(void)
{
  /* Wait for data to be received */
  while (!(UCSR0A & (1<<RXC0)))
  ;
  /* Get and return received data from buffer */
  return UDR0;
}

int main( void )
{
  UART_Init(MYUBRR);
  int receive = 0;
  
  while ((UCSR0A & (1<<RXC0)) == 0) {
    UART_Transmit(1);
    _delay_ms(100);
  }

  receive = UART_Receive();

  while(receive == 2) {
    UART_Transmit(3);
  }

}
