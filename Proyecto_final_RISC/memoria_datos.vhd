-- memoria de solo lectura

LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
USE IEEE.STD_LOGIC_ARITH.ALL;
USE IEEE.STD_LOGIC_UNSIGNED.ALL;

ENTITY memoria_datos IS
	PORT (
		clk : IN STD_LOGIC;
		direccion : IN STD_LOGIC_VECTOR (15 DOWNTO 0);
		datoW : IN STD_LOGIC_VECTOR (15 DOWNTO 0);
		memW : IN STD_LOGIC;
		datos : OUT STD_LOGIC_VECTOR (15 DOWNTO 0));
END memoria_datos;

ARCHITECTURE Behavioral OF memoria_datos IS
	TYPE memory IS ARRAY(0 TO 50) OF STD_LOGIC_VECTOR(15 DOWNTO 0);
	signal mem: memory := (
		0 => x"0001",
		1 => x"0002",
		2 => x"0004",
		3 => x"0005",
		4 => x"0001",
		5 => x"0002",
		6 => x"0006",
		7 => x"0007",
		8 => x"0009",
		9 => x"0001",
		OTHERS =>  x"0000"
	);
BEGIN
PROCESS (memW, clk)
	BEGIN
		IF (memW = '0') THEN
			datos <= mem(conv_integer(unsigned(direccion)));
		END IF;
	END PROCESS;

	PROCESS (memW, clk, datoW)
	BEGIN
		IF (falling_edge(clk)) THEN
			IF (memW = '1') THEN
				mem(conv_integer(unsigned(direccion))) <= datoW;
			END IF;
		END IF;
	END PROCESS;
END Behavioral;