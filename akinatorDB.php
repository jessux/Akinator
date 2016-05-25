<?php

	class bdd
	{
		public function bdd()
		{
			mysqli_connect();
		}

		public function setCapitaleListe()
		{
			$dictionnaire = array();
			$requete = "SELECT * FROM Capitales";

			if($ressource= $bdd::query($requete)
			{
				foreach($ressource as $result)
				{
					$dictionnaire[] = array("ID_CAPITALE" =>$result["ID_CAPITALE"], "SCORE"=>0);
				}
			}

			return $dictionnaire;
		}


		public function getCapitalesWithAttrib($attrib,$colonne)
		{
			$requete = "SEPECT ID_CAPITALE FROM ZGEG WHERE ".$colonne." = ".$attrib;

			$CapitalesResult = array();

			if($ressource = $bdd::query($requete))
			{
				foreach ($ressource as $result) {
					$CapitalesResult[] = $result["ID_CAPITALE"];
				}
			}

			return $CapitalesResult;
		}


		public function getNbCapitales()
		{
			$requete = "COUNT(*) FROM CAPITALES";
			$nb =0;
			if($ressource = $bdd::query($requete))
			{
				$nb = $ressource[0];
			}

			return $nb;
		}

		/**
		** lister:
		** @param: $table :string. Table a requeter
		** @param: $champs :tab assoc. ("champs1" => valeur,...)
		**
		** @return: tab ( tab assoc)
		**/
		function lister($table, $champs)
		{
			$requete="SELECT * FROM ".$table." WHERE ";
			$count = 0;
			foreach($champs as $key => $value)
			{
				if($count !=0)
				{
					$requete .= "AND ";
				}
				$requete .= $key ." = ". $value . " ";
			}
			$result = array();
			if($ressource= $bdd:query($requete))
			{
				while($ligne =$ressource::fetch_assoc(result))
				{
					$result[] = $ligne;
				}
			}

			return $result;
		}
	}

?>