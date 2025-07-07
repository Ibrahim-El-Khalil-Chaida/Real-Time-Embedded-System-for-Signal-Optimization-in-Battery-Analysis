# Real-Time Embedded System for Signal Optimization in Battery Analysis

[![STM32](https://img.shields.io/badge/Platform-STM32-00963e?logo=stmicroelectronics&logoColor=white)](https://www.st.com/en/microcontrollers-microprocessors/stm32-32-bit-arm-cortex-mcus.html)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-4B-red?logo=raspberrypi&logoColor=white)](https://www.raspberrypi.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0-lightgrey?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![LTspice](https://img.shields.io/badge/LTspice-Simulation-orange)](https://www.analog.com/en/design-center/design-tools-and-calculators/ltspice-simulator.html)

## Project Overview

This embedded system demonstrates optimized signal processing techniques for bioimpedance analysis or battery characterization. The system acquires signals, performs real-time optimization, and displays results through a web-based interface.

## System Architecture

```
[Analog Signal Source] → [Custom PCB]
                             ↓
                     [STM32 Microcontroller]
                             ↓
                     [Raspberry Pi]
                             ↓
               [Web Interface (HTML/CSS/Flask)]
```

### Key Components

**Member 1: PCB and Circuit Implementation**  
[![Analog Circuits](https://img.shields.io/badge/Skills-Analog%20Front%20End-FF7F50)]() [![LTspice](https://img.shields.io/badge/Tools-LTspice-orange)]()  
- Design/fabricate custom PCB for signal acquisition
- Implement analog front-end circuitry
- Perform circuit simulations in LTspice
- Create microcontroller interfaces

**Member 2: STM32 Programming**  
[![C](https://img.shields.io/badge/Language-C-blue)]() [![STM32 HAL](https://img.shields.io/badge/Library-STM32%20HAL-00963e)]()  
- Develop STM32 firmware in C
- Implement real-time signal processing
- Program digital filters
- Handle RPi communication protocols

**Member 3: Raspberry Pi Interface**  
[![Python](https://img.shields.io/badge/Language-Python-3776AB)]() [![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey)]()  
- Develop web interface with HTML/CSS
- Create data visualization dashboard
- Implement backend with Flask
- Manage data processing with Pandas

## Technology Stack

### Hardware
[![STM32F4](https://img.shields.io/badge/STM32-F4%20Series-03234B?logo=stmicroelectronics)](https://www.st.com/en/microcontrollers-microprocessors/stm32f4-series.html)
[![Raspberry Pi](https://img.shields.io/badge/RPi-4B-C51A4A?logo=raspberrypi)](https://www.raspberrypi.org/products/)

### Software
[![STM32CubeIDE](https://img.shields.io/badge/IDE-STM32CubeIDE-03234B?logo=stmicroelectronics)](https://www.st.com/en/development-tools/stm32cubeide.html)
[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.4-150458?logo=pandas)](https://pandas.pydata.org/)

### Web Technologies
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![Flask](https://img.shields.io/badge/Flask-2.0-000000?logo=flask)](https://flask.palletsprojects.com/)

## Repository Structure

```
/ProjectLab_EmbeddedSystems_SS2025/
│
├── /hardware/                 
│   ├── /schematics/            
│   └── /simulations/          
│
├── /stm32_firmware/            
│   ├── /src/                  
│   └── /docs/                 
│
├── /raspberry_pi_software/     
│   ├── /static/               
│   ├── /templates/            
│   ├── app.py                 
│   └── data_processing.py     
│
├── LICENSE                    
└── README.md                  
```

## Getting Started

### Prerequisites
[![STM32CubeIDE](https://img.shields.io/badge/Required-STM32CubeIDE-03234B)](https://www.st.com/en/development-tools/stm32cubeide.html)
[![Python 3.8](https://img.shields.io/badge/Python-3.8%2B-3776AB)](https://www.python.org/downloads/)

```bash
# Clone repository
git clone https://github.com/yourusername/ProjectLab_EmbeddedSystems_SS2025.git

# Install Python dependencies
pip install flask pandas matplotlib
```

## Documentation
- Hardware design specifications in `/hardware/docs/`
- Firmware API documentation in `/stm32_firmware/docs/`
- Web interface guide in `/raspberry_pi_software/README.md`

## Contact
Supervisor:
- Ahmed Yahia Kallel, Dr.-Ing.
- Chair for Measurement and Sensor Technology
- Reichenhainerstr. 70 Weinholdbau C25.205
- Email: ahmed-yahia.kallel@etit.tu-chemnitz.de

## License
[![MIT License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)
```

Key changes made:
1. Replaced KiCad/Altium with LTspice badges
2. Removed FreeRTOS and added STM32 HAL
3. Updated Raspberry Pi section with Flask, HTML/CSS
4. Added web technology badges (HTML5, CSS3)
5. Updated repository structure to reflect web files
6. Added specific Python library installation commands
7. Maintained consistent visual style throughout
