library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL; 

entity logica_seleccion is
	Port (  inst : in STD_LOGIC_VECTOR(1 downto 0);
			  CC : in STD_LOGIC;
			  SELECTOR : out STD_LOGIC;
			  PL : out STD_LOGIC;
			  MAP1 : Out STD_LOGIC;
			  VECT : out STD_LOGIC);
end logica_seleccion;

architecture Behavioral of logica_seleccion is
begin
	process (inst, CC)
		variable entrada : std_logic_vector(2 downto 0);
	begin
		entrada := inst & CC;
		
		case entrada is
			when "000" | "001" =>
				SELECTOR <= '0';
				PL <= '0';
				MAP1 <= '0';
				VECT <= '0';
			when "010" =>
				SELECTOR <= '0';
				PL <= '1';
				MAP1 <= '0';
				VECT <= '0';
			when "011" =>
				SELECTOR <= '1';
				PL <= '1';
				MAP1 <= '0';
				VECT <= '0';
			when "100" | "101" =>
				SELECTOR <= '1';
				PL <= '0';
				MAP1 <= '1';
				VECT <= '0';
			when "110" =>
				SELECTOR <= '0';
				PL <= '0';
				MAP1 <= '0';
				VECT <= '1';
			when "111" =>
				SELECTOR <= '1';
				PL <= '0';
				MAP1 <= '0';
				VECT <= '1';
			when others =>
		end case;
	end process;
end Behavioral;