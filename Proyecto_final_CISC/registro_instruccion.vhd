library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL; 

entity registro_instruccion is
	Port (  RELOJ : in STD_LOGIC;
			  ENA : in STD_LOGIC;
			  RESET : in STD_LOGIC;
			  ENTRADA  : in STD_LOGIC_VECTOR(7 downto 0);
			  INSTRUCT_D : out STD_LOGIC_VECTOR(7 downto 0);
			  SALIDA : out STD_LOGIC_VECTOR(11 downto 0));
end registro_instruccion;

architecture Behavioral of registro_instruccion is
signal valor_interno : std_logic_vector (11 downto 0) := X"000";
signal instruct_int : std_logic_vector(7 downto 0) := X"00";
begin
	process (RELOJ, RESET, ENTRADA, ENA)
	begin		
		if RESET = '0' then 
			valor_interno <= X"000";
		elsif falling_edge (RELOJ) and ENA = '0' then
			valor_interno <= ENTRADA & X"0";
		end if;
	end process;
	
	process (RELOJ, RESET, ENTRADA, ENA)
	begin		
		if RESET = '0' then 
			instruct_int <= X"00";
		elsif rising_edge (RELOJ) and ENA = '0' then
			instruct_int <= ENTRADA;
		end if;
	end process;
	
	process (valor_interno, instruct_int)
	begin
		INsTRUCT_D <= instruct_int;
		SALIDA <= valor_interno;
	end process;
	
	
end Behavioral;