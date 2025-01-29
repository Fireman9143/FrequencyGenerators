#include <Wire.h>
#include <si5351.h>

// Create an instance of Si5351
Si5351 si5351;

void setup() {
    Serial.begin(115200);  // Start Serial communication
    Serial.println("Initializing Si5351A...");

    // Initialize Si5351 with a 25MHz crystal
    if (!si5351.init(SI5351_CRYSTAL_LOAD_8PF, 25000000, 0)) {  
        Serial.println("Si5351A not found! Check wiring.");
        while (1);  // Halt execution if the module is not detected
    }

    Serial.println("Si5351A detected. Setting frequencies...");

    // Set CLK0 to 8.8 MHz (8,800,000 Hz)
    si5351.set_freq(8800000ULL, SI5351_CLK0);

    // Set CLK1 to 14.175 MHz (14,175,000 Hz)
    si5351.set_freq(14175000ULL, SI5351_CLK1);

    // Set CLK2 to 60 MHz (60,000,000 Hz)
    si5351.set_freq(60000000ULL, SI5351_CLK2);

    // Set maximum drive strength for all channels
    si5351.drive_strength(SI5351_CLK0, SI5351_CLK_DRIVE_STRENGTH_8MA);
    si5351.drive_strength(SI5351_CLK1, SI5351_CLK_DRIVE_STRENGTH_8MA);
    si5351.drive_strength(SI5351_CLK2, SI5351_CLK_DRIVE_STRENGTH_8MA);

    Serial.println("CLK0 set to 8.8 MHz");
    Serial.println("CLK1 set to 14.175 MHz");
    Serial.println("CLK2 set to 60 MHz");
}

void loop() {
    // Send frequency values to Serial Plotter for monitoring
    Serial.print(8.8);
    Serial.print(",");
    Serial.print(14.175);
    Serial.print(",");
    Serial.println(60);
    delay(100); // Adjust for smooth plotting
}

