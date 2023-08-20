#include "mbed.h"
#include "chrono"
#include <cstdlib>

DigitalOut my_led(PA_10);
DigitalIn my_button(PC_13); 

BufferedSerial pc(USBTX, USBRX); 
FileHandle *mbed::mbed_override_console(int fd) {
    return &pc;
}

int main() {
    my_led = 0; 
    printf("Press the user button when the LED lights up\n");

    while (1) {
        int delay = (std::rand() % 4) + 2;

        ThisThread::sleep_for(std::chrono::seconds(delay));

        my_led = 1;

        auto start = std::chrono::system_clock::now();
        while (my_button == 1) {}
        auto end = std::chrono::system_clock::now();
        std::chrono::duration<double> diff = end-start;

        my_led = 0;

        double reaction_time = diff.count();
        int int_part = (int) reaction_time;

        printf("Your reaction time was: %d seconds\n", int_part);

        for (int i = 0; i < int_part; i++) {
            my_led = 1;
            ThisThread::sleep_for(std::chrono::milliseconds(200));
            my_led = 0;
            ThisThread::sleep_for(std::chrono::milliseconds(200));
        }

        ThisThread::sleep_for(std::chrono::seconds(1));

        for (int i = 0; i < 3; i++) {
            my_led = 1;
            ThisThread::sleep_for(std::chrono::milliseconds(500));
            my_led = 0;
            ThisThread::sleep_for(std::chrono::milliseconds(500));
        }

        ThisThread::sleep_for(std::chrono::seconds(1));
    }
}
