<?php

include "akinatorDB.php";
include "akinator.php";

	Class question
	{
		private $id_;
		private $questions_posees_;
		private $questions_a_venir_;

		private $bdd_;
		private $moteur_;

		function question()
		{
			$bdd_ = new bdd();
			$id_= rand(0,$bdd_->get_max_question()); //<-fonctions à faire lol
			$questions_a_venir_ = $bdd_-> init_questions(); //<-fonctions à faire lol
			$questions_posees_ = array();

		}

		function poserQuestion()
		{
			foreach ($questions_a_venir_ as $question)
			{
				if($question.get_id() != $id_)
				{
					$id_= nextQuestion($);
				}
			}
		}

		function nextQuestion()
		{
			
		}
	}

?>