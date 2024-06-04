#include "stm32f4xx.h"
#include "stm32f4xx_nucleo.h"

#include "drv_uart.h"
#include "dynamixel.h"

extern uint8_t car_received;

int main(void)
{
	HAL_Init();	// passage par stm32f4xx_hal_msp.c : configuration des broches
	SystemClock_Config();

	HAL_MspInit();
    uart1_Init();			// ZIGBEE
    uart2_Init();           // CABLE
    uart6_Init();           // DYNAMIXEL
    HAL_Delay(500);

	dxl_LED(1, LED_ON);
	HAL_Delay(500);
	dxl_LED(1, LED_OFF);
	HAL_Delay(500);
	dxl_LED(1, LED_ON );
	HAL_Delay(500);
	dxl_LED(1, LED_OFF);
	HAL_Delay(500);

	dxl_setOperatingMode(1, VELOCITY_MODE);
	dxl_torque(1, TORQUE_ON);
	dxl_setGoalVelocity(1, 0);
	dxl_setOperatingMode(2, VELOCITY_MODE);
		dxl_torque(2, TORQUE_ON);
		dxl_setGoalVelocity(2, 0);
		uint16_t v = 100;
		uint16_t dv = 50;
		uint16_t last_state = 0;
		uint16_t i=0;
		uint8_t mode = 0;
		uint16_t del = 0;
		uint16_t vbuffer[6];
		char path[300];
	    while(1)
	    {


	    	if( car_received == 'z')
	    	{
	    		last_state = 'z';
	    		dxl_setGoalVelocity(1, v);
	    		dxl_setGoalVelocity(2, -v);
	    	}
	    	else if (car_received == 'd')
	    	{
	    		last_state = 'd';
	    		dxl_setGoalVelocity(1, v);
	    			    		dxl_setGoalVelocity(2, 0);
	    	}
	    	else if (car_received == 'q')
	        {
	    		last_state = 'q';
	    		   dxl_setGoalVelocity(1, 0);
	    		   dxl_setGoalVelocity(2,-v);
	      }
	    	else if( car_received == 's')
	    	{
	    		last_state = 's';
	    		dxl_setGoalVelocity(1,-v);
	    		dxl_setGoalVelocity(2, v);
	    	}


	    	else if (car_received == 'v'){
	    		mode = 1;

	    	    	}
	    	else if (car_received == 'p'){
	    		mode = 2;
	    	}
	    	else if (car_received == 'j'){
	    		if((HAL_GPIO_ReadPin(GPIOA,GPIO_PIN_8))&(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_5))){
	    			    		    			dxl_setGoalVelocity(1, v);
	    			    		    			dxl_setGoalVelocity(2,-v);
	    			    		    		}
	    			    		    		else if((HAL_GPIO_ReadPin(GPIOA,GPIO_PIN_8))){
	    			    		    			dxl_setGoalVelocity(1, -dv);
	    			    		    			dxl_setGoalVelocity(2,-dv);
	    			    		    		}
	    			    		    		else if((HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_5))){
	    			    		    			    			dxl_setGoalVelocity(1, dv);
	    			    		    			    			dxl_setGoalVelocity(2,dv);
	    			    		    			    		}
	    			    		    		else {
	    			    		    			dxl_setGoalVelocity(1, 0);
	    			    		    			dxl_setGoalVelocity(2,0);
	    			    		    		}
	    	}


	    	else {
	    		dxl_setGoalVelocity(1, 0);
	    			    		   dxl_setGoalVelocity(2,0);
	    	}
	    	if ((mode == 1) & (car_received>='0') & (car_received <='9') ){
	    		if(i<2)
	    		{
	    			vbuffer[i] = car_received-'0';
	    			i++;
	    			car_received= 0 ;
	    		}
	    			else {
	    			vbuffer[i] = car_received-'0';
	    			v =vbuffer[0]*100+vbuffer[1]*10+vbuffer[2];
	    			i = 0;
	    			car_received = last_state;
	    			mode = 0;
	    		}
	    	}
	    	else if ((mode == 2)& (car_received != 0)){
	    		path[i] = car_received;

	    		i++;
	    		if((car_received == 'l') || (car_received == 'r')){
	    		uint8_t loop = 1;
	    		while (loop){
	    		if (path[i]=='l') loop =0;
	    			for(int j =0 ; j<i ; j ++){
	    				if(path[j] == 'a'){
	    					dxl_setGoalVelocity(1, 150);
	    					dxl_setGoalVelocity(2, -150);
	    					 HAL_Delay(1000);
	    					 dxl_setGoalVelocity(1, 0);
	    					 	    					dxl_setGoalVelocity(2, 0);
	    				}
	    				else if (path[j] == 'e'){

	    					dxl_setGoalVelocity(1, -150);
	    						dxl_setGoalVelocity(2, -150);

	    						 HAL_Delay(350);
	    						 dxl_setGoalVelocity(1, 0);
	    							    					 	    					dxl_setGoalVelocity(2, 0);
	    				}
	    				else if (path[j] == 't'){

	    					    					dxl_setGoalVelocity(1, 150);
	    					    						dxl_setGoalVelocity(2, 150);

	    					    						 HAL_Delay(350);
	    					    						 dxl_setGoalVelocity(1, 0);
	    					    						dxl_setGoalVelocity(2, 0);
	    					    				}
	    				else if (car_received =='o'){
	    					loop=0;
	    					break;
	    				}

	    			}

	    			}

	    			car_received= 0 ;
	    			mode = 0 ;
	    		}
	    		car_received= 0 ;
	    	}

	    	int32_t v1 =dxl_getPresentVelocity(1);
	    	int32_t v2 =dxl_getPresentVelocity(2);

	    		v1 = -v1;
	    		v2 = -v2;
	    	term_printf_zigbee("%d %d",v1,v2);

	        HAL_Delay(10);

	    }
	    return 0;
}
//=====================================================================================
