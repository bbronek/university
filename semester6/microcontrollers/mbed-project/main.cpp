#include "mbed.h"
#include <chrono>
#include <cstdlib>

DigitalOut led(PA_10);
DigitalIn button(PC_13);

BufferedSerial pc(USBTX, USBRX);
FileHandle *mbed::mbed_override_console(int) { return &pc; }

int main() {
    led = 0;
    printf("Press the user button when the LED lights up\n");

    while (true) {
        while (button == 0) {
            ThisThread::sleep_for(std::chrono::milliseconds(1));
        }
        int delay = (std::rand() % 4) + 2;

        ThisThread::sleep_for(std::chrono::seconds(delay));

        led = 1;

        auto start = std::chrono::steady_clock::now();
        while (button == 1) {
            ThisThread::sleep_for(std::chrono::milliseconds(1));
        }
        auto end = std::chrono::steady_clock::now();
        std::chrono::duration<double> diff = end - start;

        led = 0;

        double reaction_time = diff.count();
        int int_part = (int)reaction_time;

        printf("Your reaction time was: %d milliseconds\n", static_cast<int>(reaction_time * 1000));

        for (int i = 0; i < int_part; i++) {
            led = 1;
            ThisThread::sleep_for(std::chrono::milliseconds(200));
            led = 0;
            ThisThread::sleep_for(std::chrono::milliseconds(200));
        }

        ThisThread::sleep_for(std::chrono::seconds(1));

        for (int i = 0; i < 3; i++) {
            led = 1;
            ThisThread::sleep_for(std::chrono::milliseconds(500));
            led = 0;
            ThisThread::sleep_for(std::chrono::milliseconds(500));
        }

        ThisThread::sleep_for(std::chrono::seconds(1));
    }
}
