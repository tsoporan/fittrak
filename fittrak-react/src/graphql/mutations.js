import gql from "graphql-tag";

const addCustomExerciseMutation = gql`
  mutation addCustomExercise(
    $workoutId: Int!
    $exerciseName: String!
    $muscleGroupName: String!
  ) {
    addCustomExercise(
      workoutId: $workoutId
      exerciseName: $exerciseName
      muscleGroupName: $muscleGroupName
    ) {
      exercise {
        id
        slug
        name
        dateStarted
        dateEnded
        workout {
          id
        }
      }
    }
  }
`;

const updateViewerMutation = gql`
  mutation updateSettings(
    $height: Float
    $weight: Float
    $preferredUnit: UnitEnumType!
  ) {
    updateSettings(
      height: $height
      weight: $weight
      preferredUnit: $preferredUnit
    ) {
      viewer {
        id
        profile {
          height
          weight
          preferredUnit
        }
      }
    }
  }
`;

const removeExerciseMutation = gql`
  mutation removeExercise($exerciseId: Int!) {
    removeExercise(exerciseId: $exerciseId) {
      exercise {
        id
      }
    }
  }
`;

const updateWorkoutMutation = gql`
  mutation updateWorkout(
    $workoutId: Int!
    $workoutFields: WorkoutFieldInputType!
  ) {
    updateWorkout(workoutId: $workoutId, workoutFields: $workoutFields) {
      workout {
        id
        dateEnded
        dateStarted
        status
      }
    }
  }
`;

const removeWorkoutMutation = gql`
  mutation removeWorkout($workoutId: Int!) {
    removeWorkout(workoutId: $workoutId) {
      workout {
        id
        isActive
      }
    }
  }
`;

const createWorkoutMutation = gql`
  mutation createWorkout {
    createWorkout {
      workout {
        id
        slug
        dateStarted
        dateEnded
        exercises {
          id
        }
        isActive
        status
        exerciseCount
      }
    }
  }
`;

const addExercisesMutation = gql`
  mutation addExercises($workoutId: Int!, $exercises: [ExerciseInputType!]!) {
    addExercises(workoutId: $workoutId, exercises: $exercises) {
      exercises {
        id
        slug
        name
        dateStarted
        dateEnded
        sets {
          id
          weight
          repetitions
          unit
          bodyweight
        }
        workout {
          id
        }
      }
    }
  }
`;

const updateSetMutation = gql`
  mutation updateSet($setId: Int!, $setFields: SetFieldInputType!) {
    updateSet(setId: $setId, setFields: $setFields) {
      set {
        id
        weight
        repetitions
        unit
        isActive
        bodyweight
      }
    }
  }
`;

const removeSetMutation = gql`
  mutation removeSet($setId: Int!) {
    removeSet(setId: $setId) {
      set {
        id
        exercise {
          id
        }
      }
    }
  }
`;

const addSetMutation = gql`
  mutation addSet(
    $exerciseId: Int!
    $repetitions: Int!
    $weight: Int!
    $unit: String!
    $bodyweight: Boolean
  ) {
    addSet(
      exerciseId: $exerciseId
      repetitions: $repetitions
      weight: $weight
      unit: $unit
      bodyweight: $bodyweight
    ) {
      set {
        id
        repetitions
        weight
        unit
        bodyweight
        exercise {
          id
        }
      }
    }
  }
`;

export default {
  addCustomExerciseMutation,
  updateViewerMutation,
  removeExerciseMutation,
  updateWorkoutMutation,
  removeWorkoutMutation,
  createWorkoutMutation,
  addExercisesMutation,
  updateSetMutation,
  removeSetMutation,
  addSetMutation
};
