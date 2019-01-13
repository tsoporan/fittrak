import gql from "graphql-tag";

const viewerQuery = gql`
  query viewer {
    viewer {
        id
        username
        email
        profile {
          height
          weight
          preferredUnit
        }
    }
`;

const workoutsQuery = gql`
  query workouts($status: WorkoutStatusesEnum, $limit: Int) {
    workouts(status: $status, limit: $limit) {
      id
      dateStarted
      dateEnded
      status
      slug
    }
  }
`;

const workoutQuery = gql`
  query workout($workoutId: Int!) {
    workout(workoutId: $workoutId) {
      id
      status
      dateStarted
      dateEnded
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
        }
      }
    }
  }
`;

const exerciseTypesQuery = gql`
  query exerciseTypes {
    exerciseTypes {
      id
      name
    }
  }
`;

const muscleGroupsQuery = gql`
  query muscleGroups {
    muscleGroups {
      id
      name
    }
  }
`;

const exercisesQuery = gql`
  query exercises($workoutId: Int!) {
    exercises(workoutId: $workoutId) {
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
`;

const exerciseQuery = gql`
  query exercise($exerciseId: Int!) {
    exercise(exerciseId: $exerciseId) {
      id
      sets {
        id
        weight
        repetitions
        unit
        bodyweight
      }
    }
  }
`;

const setsQuery = gql`
  query sets($exerciseId: Int!) {
    sets(exerciseId: $exerciseId) {
      id
      weight
      repetitions
      unit
      bodyweight
      exercise {
        id
      }
    }
  }
`;

export default {
  viewerQuery,
  exerciseTypesQuery,
  muscleGroupsQuery,
  workoutsQuery,
  workoutQuery,
  exercisesQuery,
  exerciseQuery,
  setsQuery
};
