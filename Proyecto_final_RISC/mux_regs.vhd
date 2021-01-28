LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;

ENTITY mux_regs IS
	PORT (
		selregr : IN STD_LOGIC_VECTOR(3 DOWNTO 0);
		selregW : IN STD_LOGIC_VECTOR(2 DOWNTO 0);
		ACCA : IN STD_LOGIC_VECTOR(15 DOWNTO 0);
		ACCB : IN STD_LOGIC_VECTOR(15 DOWNTO 0);
		IX : IN STD_LOGIC_VECTOR(15 DOWNTO 0);
		IY : IN STD_LOGIC_VECTOR(15 DOWNTO 0);
		SP : IN STD_LOGIC_VECTOR(15 DOWNTO 0);
		AUX : IN STD_LOGIC_VECTOR(15 DOWNTO 0);
		DatoW : IN STD_LOGIC_VECTOR(15 DOWNTO 0);
		D1 : OUT STD_LOGIC_VECTOR(15 DOWNTO 0);
		D2 : OUT STD_LOGIC_VECTOR(15 DOWNTO 0));
END mux_regs;

ARCHITECTURE Behavioral OF mux_regs IS
BEGIN
	PROCESS (selregr, ACCA, ACCB, IX, IY, SP, AUX)
	BEGIN
		IF selregW = "001" AND selregr "0001" THEN
			D1 <= DatoW;
			D2 <= ACCB;
		ELSIF elregW = "100" AND selregr "0001" THEN
			D1 <= ACCA;
			D2 <= DatoW;
		ELSIF elregW = "100" AND selregr "0010" THEN
			D1 <= DatoW;
			D2 <= IX;
		ELSIF elregW = "010" AND selregr "0010" THEN
			D1 <= ACCB;
			D2 <= DatoW;
		ELSIF elregW = "100" AND selregr "0011" THEN
			D1 <= DatoW;
			D2 <= IY;
		ELSIF elregW = "011" AND selregr "0011" THEN
			D1 <= ACCB;
			D2 <= DatoW;
		ELSIF elregW = "001" AND selregr "0100" THEN
			D1 <= DatoW;
			D2 <= '0';
		ELSIF elregW = "100" AND selregr "0101" THEN
			D1 <= DatoW;
			D2 <= '0';
		ELSIF elregW = "001" AND selregr "0110" THEN
			D1 <= DatoW;
			D2 <= IX;
		ELSIF elregW = "010" AND selregr "0110" THEN
			D1 <= ACCA;
			D2 <= DatoW;
		ELSIF elregW = "001" AND selregr "0111" THEN
			D1 <= DatoW;
			D2 <= IY;
		ELSIF elregW = "011" AND selregr "0111" THEN
			D1 <= ACCA;
			D2 <= DatoW;
		ELSIF elregW = "101" AND selregr "1000" THEN
			D1 <= DatoW;
			D2 <= '0';
		ELSIF elregW = "010" AND selregr "0010" THEN
			D1 <= '0';
			D2 <= DatoW;
		ELSIF elregW = "011" AND selregr "0011" THEN
			D1 <= '0';
			D2 <= DatoW;
		ELSIF elregW = "110" AND selregr "0110" THEN
			D1 <= '0';
			D2 <= DatoW;
		ELSIF elregW = "001" AND selregr "0001" THEN
			D1 <= DatoW;
			D2 <= SP;
		ELSIF elregW = "110" AND selregr "0110" THEN
			D1 <= ACCA;
			D2 <= DatoW;
		ELSIF elregW = "100" AND selregr "0100" THEN
			D1 <= DatoW;
			D2 <= ACCB;
		ELSIF elregW = "110" AND selregr "0110" THEN
			D1 <= DatoW;
			D2 <= ACCB;
		ELSIF elregW = "010" AND selregr "0010" THEN
			D1 <= DatoW;
			D2 <= ACCB;
		ELSIF elregW = "011" AND selregr "0110" THEN
			D1 <= DatoW;
			D2 <= ACCB;
		ELSIF elregW = "011" AND selregr "0011" THEN
			D1 <= DatoW;
			D2 <= ACCB;
		ELSIF elregW = "011" AND selregr "0110" THEN
			D1 <= DatoW;
			D2 <= ACCB;
		ELSIF selregr = "0000" THEN
			D1 <= (OTHERS => '0');
			D2 <= (OTHERS => '0');
		ELSIF selregr = "0001" THEN
			D1 <= ACCA;
			D2 <= ACCB;
		ELSIF selregr = "0010" THEN
			D1 <= ACCB;
			D2 <= IX;
		ELSIF selregr = "0011" THEN
			D1 <= ACCB;
			D2 <= IY;
		ELSIF selregr = "0100" THEN
			D1 <= ACCA;
			D2 <= X"0000";
		ELSIF selregr = "0101" THEN
			D1 <= ACCB;
			D2 <= X"0000";
		ELSIF selregr = "0110" THEN
			D1 <= ACCA;
			D2 <= IX;
		ELSIF selregr = "0111" THEN
			D1 <= ACCA;
			D2 <= IY;
		ELSIF selregr = "1000" THEN
			D1 <= AUX;
			D2 <= X"0000";
		ELSIF selregr = "1001" THEN
			D1 <= X"0000";
			D2 <= IX;
		ELSIF selregr = "1010" THEN
			D1 <= X"0000";
			D2 <= IY;
		ELSIF selregr = "1011" THEN
			D1 <= X"0000";
			D2 <= SP;
		ELSIF selregr = "1100" THEN
			D1 <= ACCA;
			D2 <= SP;
		ELSIF selregr = "1101" THEN
			D1 <= ACCB;
			D2 <= SP;
		ELSIF selregr = "1110" THEN
			D1 <= IX;
			D2 <= SP;
		ELSIF selregr = "1111" THEN
			D1 <= IY;
			D2 <= SP;
		ELSE
			D1 <= (OTHERS => '0');
			D2 <= (OTHERS => '0');
		END IF;
	END PROCESS;
END Behavioral;