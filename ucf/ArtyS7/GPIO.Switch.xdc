## =============================================================================================================================================================
## Xilinx Design Constraint File (XDC)
## =============================================================================================================================================================
## Board:         Digilent - Arty_S7
## FPGA:          Xilinx Artix 7
## =============================================================================================================================================================
## General Purpose I/O 
## =============================================================================================================================================================
## Switch
## =============================================================================================================================================================
## -----------------------------------------------------------------------------
##	Bank:			15,34			
##		VCCO:		VCC3V3			
##	Location:		SW0,SW1,SW2,SW3			
## -----------------------------------------------------------------------------
## {IN}    SW0
set_property PACKAGE_PIN  H14      [ get_ports Arty_S7_GPIO_Switch[0] ]	#IO_L20N_T3_A19_15
## {IN}    SW1
set_property PACKAGE_PIN  H18      [ get_ports Arty_S7_GPIO_Switch[1] ]	#IO_L21P_T3_DQS_15
## {IN}    SW2
set_property PACKAGE_PIN  G18      [ get_ports Arty_S7_GPIO_Switch[2] ]	#IO_L21N_T3_DQS_A18_15
## {IN}    SW3
set_property PACKAGE_PIN  M5       [ get_ports Arty_S7_GPIO_Switch[3] ]	#IO_L6N_T0_VREF_34