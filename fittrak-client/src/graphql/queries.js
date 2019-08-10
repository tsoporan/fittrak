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
  }
`;

const workoutsQuery = gql`
  query workouts($status: WorkoutStatusesEnum, $limit: Int) {
    workouts(status: $status, limit: $limit) {
      id
      startedAt
      endedAt
      status
      slug
      exerciseCount
    }
  }
`;

const workoutQuery = gql`
  query workout($workoutId: Int!) {
    workout(workoutId: $workoutId) {
      id
      status
      startedAt
      endedAt
      exercises {
        id
        slug
        name
        startedAt
        endedAt
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

const popularExerciseTypesQuery = gql`
  query popularExerciseTypes {
    popularExerciseTypes {
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
      startedAt
      endedAt
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
  popularExerciseTypesQuery,
  muscleGroupsQuery,
  workoutsQuery,
  workoutQuery,
  exercisesQuery,
  exerciseQuery,
  setsQuery
};
