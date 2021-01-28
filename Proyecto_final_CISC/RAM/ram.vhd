LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
USE IEEE.STD_LOGIC_ARITH.ALL;
USE IEEE.STD_LOGIC_UNSIGNED.ALL;

ENTITY ram IS
	PORT (
		address : IN STD_LOGIC_VECTOR(15 DOWNTO 0);
		data : INOUT STD_LOGIC_VECTOR(7 DOWNTO 0);
		Wn : IN STD_LOGIC;
		CSn : IN STD_LOGIC
	);
END ram;

ARCHITECTURE Behavioral OF ram IS
	TYPE memory IS ARRAY(0 TO 63) OF STD_LOGIC_VECTOR(7 DOWNTO 0);
	SIGNAL mem : memory;
	SIGNAL data_out : STD_LOGIC_VECTOR(7 DOWNTO 0) := X"00";

BEGIN

	-- Memory Write Block
	MEM_WRITE : PROCESS (address, CSn, Wn, data)
	BEGIN
		mem(0) <= x"7E";
		mem(1) <= x"00";
		mem(2) <= x"0D";
		mem(3) <= x"00";
		mem(4) <= x"09";
		mem(5) <= x"04";
		mem(6) <= x"05";
		mem(7) <= x"01";
		mem(8) <= x"02";
		mem(9) <= x"06";
		mem(10) <= x"07";
		mem(11) <= x"09";
		mem(12) <= x"01";
		mem(13) <= x"86";
		mem(14) <= x"00";
		mem(15) <= x"C6";
		mem(16) <= x"FF";
		mem(17) <= x"CE";
		mem(18) <= x"04";
		mem(19) <= x"A5";
		mem(20) <= x"25";
		mem(21) <= x"03";
		mem(22) <= x"7E";
		mem(23) <= x"00";
		mem(24) <= x"26";
		mem(25) <= x"AB";
		mem(26) <= x"00";
		mem(27) <= x"08";
		mem(28) <= x"8C";
		mem(29) <= x"0C";
		mem(30) <= x"27";
		mem(31) <= x"03";
		mem(32) <= x"7E";
		mem(33) <= x"00";
		mem(34) <= x"13";
		mem(35) <= x"7E";
		mem(36) <= x"00";
		mem(37) <= x"30";
		mem(38) <= x"E0";
		mem(39) <= x"00";
		mem(40) <= x"08";
		mem(41) <= x"8C";
		mem(42) <= x"0C";
		mem(43) <= x"27";
		mem(44) <= x"03";
		mem(45) <= x"7E";
		mem(46) <= x"00";
		mem(47) <= x"13";
		mem(48) <= x"AD";
		mem(49) <= x"7E";
		mem(50) <= x"00";
		mem(51) <= x"0C";
		IF (CSn = '0' AND Wn = '0') THEN
			mem(conv_integer(unsigned(address))) <= data;
		END IF;
	END PROCESS;

	TRI_STATE : PROCESS (address, CSn, Wn, data_out)
	BEGIN
		IF (CSn = '0' AND Wn = '1') THEN
			data <= data_out;
		ELSE
			data <= (OTHERS => 'Z');
		END IF;
	END PROCESS;

	-- Memory Read Block
	MEM_READ : PROCESS (address, CSn, Wn, mem)
	BEGIN
		IF (CSn = '0' AND Wn = '1') THEN
			data_out <= mem(conv_integer(unsigned(address)));
		ELSE
			data_out <= (OTHERS => '0');
		END IF;
	END PROCESS;

END Behavioral;