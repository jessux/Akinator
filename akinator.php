<?php


	/*imports*/

	class Moteur
	{
		private scoreTab = array();

		public function moteur($bdd)
		{
			scoreTab = $bdd:setCapitaleListe();

		}

		public function getMaxScore()
		{
			$maxi = 0;
			$Capitale = array();

			foreach ($dictionnaire as $score) {
				if($score["SCORE"]>$maxi)
				{
					$maxi=($score["SCORE"]);
					$Capitale= {$score["ID_CAPITALE"]};
				}
				else if($score["SCORE"]==$maxi)
				{
					$Capitale[] = {$score["ID_CAPITALE"]};
				}
			}
			return $Capitale;
		}

		public function getProbaFind($bdd)
		{
			$liste = getMaxScore();

			$result = 100.0-(count($liste)/$bdd::getNbCapitales())*100;

			return $result;
		}

		public function getNbVillesReponse()
		{
			return count(getMaxScore());
		}

		public function updateScore($score,$colonne,$attribut,$bdd)
		{
			$requete = "SELECT ID_CAPITALE FROM ZGEG WHERE ".$colonne." = ".$attribut;		
			if($ressource = $bdd::query($requete))
			{
				foreach ($ressource as $result) {
					$scoreTab[$result["ID_CAPITALE"]] += 2;

				}
			}
		}

	}
?>